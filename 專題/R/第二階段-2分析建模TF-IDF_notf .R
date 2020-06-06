#================================讀檔======================
library(readr)
setwd("F:/資策會/專題/個人資料/第四階段")
avg_data_ID=read_csv("C:/Users/sky/iii_ETL/fasttext_allpeoplecut1230_cut1230_v17_w5_sg0_min3_i10_no_around_AVG.csv")
#原本以為是python那邊檔案處理輸出的編碼問題，就不停的嘗試用df或者numpy存CSV
#都不行，又回去原使資料剛拉進來的ETL直接存CSV，還是到這邊解碼會失敗，嘗試加入
#encoding="utf-8"或fileencoding="utf-8"或者用nopad++檢查是不是BOM檔,最後找到的
#折衷辦法是nopad++存BOM檔，再用excel存成xls用library(readxl)讀取,才成功
#但是一定有CSV也能讀的方式，後來才找到套件library(readr)，直接用讀取中文字了
#估計是原生的R中文編碼太舊，讓我遮疼了很久
#avg_data_ID=read.csv("C:/Users/sky/iii_ETL/avg6.csv",header = T,encoding ="UTF-8")
#avg_data_ID=read_excel("F:/資策會/專題/爬蟲/venv/BOOMfree_food_clean_id_recipename_ingredientnames_number_unit.xls")

#==============================遺漏值=======================
#原本以為每個文本都一定有向量，所以要直接進PCA降維，發現報錯有遺漏值，原本想不通後來用套件檢查發現
#檢查遺漏
any(is.na(avg_data_ID))
#觀察遺漏值  數字太固定 懷疑有幾筆資料消失 所以決定直接整筆刪除
library(VIM)
library(missForest)
miss_plot=aggr(avg_data_ID,col=c("blue","red"),number=TRUE,sortVars=TRUE,gap=0.1,labels=names(avg_data_ID),ylab=c("Miss_data","Pattern"))
#刪除空的紀錄
avg_complete=avg_data_ID[complete.cases(avg_data_ID),]
miss_plot=aggr(avg_complete,col=c("blue","red"),number=TRUE,sortVars=TRUE,gap=0.1,labels=names(avg_complete),ylab=c("Miss_data","Pattern"))
#沒有做PCA
# 
#==============================PCA=============================
#PCA=>無法劃出累積資訊圖
library(C50)
input_pca_data=avg_complete[,c(-1,-2)]
#所以可以忽略正規化問題 離群值煩惱
#center: 預設值為TRUE。表示將資料平均值置中為0。
#scale: 預設值為TRUE。表示將資料標準差壓縮為1
pca_avg=princomp(input_pca_data)
summary(pca_avg)
screeplot(pca_avg,type="line")
plot(pca_avg)

#手動算出PVE 為了之後能做累積比例圖,由sdev標準差算出變異數的比例PVE
VE=pca_avg$sdev^2
PVE=VE/sum(VE)
Cumulative_vector=c()
names(PVE)=1:length(PVE)

for(i in 1:length(PVE)){
  base_vector=0
  for(j in 1:i){
    base_vector=base_vector+PVE[j]
  }
  Cumulative_vector=c(Cumulative_vector,base_vector)
}
vector_id=1:17
PVE_Cumulative_DF=data.frame(vector_id,PVE,Cumulative_vector)

#畫出PVE與CPVE圖
library(esquisse)
#esquisse::esquisser()
library(ggplot2)
library(ggthemes)
#PVE
ggplot(PVE_Cumulative_DF) +
  aes(x = vector_id,y=Cumulative_vector) +
  #geom_line(aes(x = vector_id,y=PVE),colour = "blue")+
  geom_point(aes(x = vector_id,y=PVE),colour = "blue")+
  labs(x = "主要成分(Principal Components)", y = "Proportion(比例)", title = " Variance Explained(解釋變數)")+ theme_gdocs()
#CPVE
ggplot(PVE_Cumulative_DF) +
 aes(x = vector_id,y=Cumulative_vector) +
 geom_point(aes(x = vector_id,y=Cumulative_vector),colour = "#ff0055") +
 geom_line(aes(x = vector_id,y=PVE),colour = "blue")+
 labs(x = "主要成分(Principal Components)", y = "Proportion(比例)", title = "Cumulative of Variance Explained(累積)")+ theme_gdocs()
#原本想找一條已經有的函數來解釋
#stat_function(fun=function(x) log(x, base =1400)+0.27)+

#  取5=>7成
compose=predict(pca_avg)
compose5=compose[,c(1:5)]
avg_complete=cbind(avg_complete,compose5)

# #============================階層式分群(bottom-up)=====================
# #62變數+歐式只有沃德和complete能用==>一張一張看   笨蛋!!!!!
hc=hclust(dist(avg_complete[,-seq(from=1,to=19)], method="euclidean"), method="ward.D2")
hc=hclust(dist(avg_complete[,-seq(from=1,to=19)], method="euclidean"), method="single")
hc=hclust(dist(avg_complete[,-seq(from=1,to=19)], method="euclidean"), method="complete")
hc=hclust(dist(avg_complete[,-seq(from=1,to=19)], method="euclidean"), method="average")
hc=hclust(dist(avg_complete[,-seq(from=1,to=19)], method="euclidean"), method="centroid")
hc=hclust(dist(avg_complete[,-seq(from=1,to=19)], method="manhattan"), method="ward.D2")
hc=hclust(dist(avg_complete[,-seq(from=1,to=19)], method="manhattan"), method="complete")
plot(hc,hang =-0.01, cex=0.1)
fit =cutree(hc, k =3)
#將結果合併回去
avg_complete=cbind(avg_complete,fit)
rect.hclust(hc, k =3, border="red")

write_csv(avg_complete,"F:/資策會/專題/R跟jupyternotebook_code/complete.csv")

# 
# #目標找到分群結果之間數量不會差異太大
# #@@@@@@@@@@@@@@@@BT_k=3 看資料用的DF
BT_k_3=function(data,group_k){
 group_dist=list("ward.D2","single","complete","average","centroid")
 point_dist=list("euclidean","manhattan","maximum","canberra")
 BT_k_3_see=data.frame(k=c(1,2,3))
  for (j in  point_dist){
   for (i in  group_dist){
     for (k in 1:group_k){}
    hc=hclust(dist(data, method=j), method=i)
    fit =cutree(hc, k =3)
    # #條件找k=1,2,3   算出比例=個數/總數
    new=data.frame(c(sum(fit==1)/nrow(avg_complete),sum(fit==2)/nrow(avg_complete),sum(fit==3)/nrow(avg_complete)))
    colnames(new)=paste(i,j,sep="+")
    BT_k_3_see=cbind(BT_k_3_see,new)
    }
  }
 return(BT_k_3_see)
}
BT=BT_k_3(avg_complete[,-seq(from=1,to=19)],3)
# #@@@@@@@@@@@@@@@@BT_k=3畫圖用的DF
# BT_k_3_graph=data.frame()
# group_dist=list("ward.D2","single","complete","average","centroid")
# point_dist=list("euclidean","manhattan","maximum","canberra")
# for (j in  point_dist){
#   for(i in  group_dist){
#     hc=hclust(dist(avg_complete[,-seq(from=1,to=252)], method=j), method=i)
#     fit =cutree(hc, k =3)
#     # #條件找k=1,2,3   算出比例=個數/總數
#     new1=data.frame(values=c(sum(fit==1)/nrow(avg_complete)),G="G1",method=paste(substring(i,1,3),substring(j,1,3),sep="+"))
#     new2=data.frame(values=c(sum(fit==2)/nrow(avg_complete)),G="G2",method=paste(substring(i,1,3),substring(j,1,3),sep="+"))
#     new3=data.frame(values=c(sum(fit==3)/nrow(avg_complete)),G="G3",method=paste(substring(i,1,3),substring(j,1,3),sep="+"))
#     BT_k_3_graph=rbind(BT_k_3_graph,new1,new2,new3)
#   }
# }

#k=3 沃德法+曼哈頓 比例圖 ===>想讓線更平，組數分布的更平均，聯想到變異數  這些DATA離散的情況
ggplot(BT) +
  aes(x = k, y = `ward.D2+manhattan`) +
  geom_line(size = 1L, colour = "#d94801") +
  labs(x = "Group=3", y = "比例", title = "Ward.D2+manhattan ") +
  theme_stata()


#從前面的一個一個參數到寫成迴圈 再到一次出兩種DF
BT_function=function(data,group_k){
  group_dist=list("ward.D2","single","complete","average","centroid")
  point_dist=list("euclidean","manhattan","maximum","canberra")
  dfA=data.frame(k=1:group_k)
  dfB=data.frame()
  for (j in  point_dist){
    for (i in  group_dist){
      hc=hclust(dist(data, method=j), method=i)
      fit =cutree(hc, k =group_k)
      #============A第一個表格先做統計用途
      #要先用一個暫時的df疊加單筆的不同群values
      tmp=data.frame()
      for (k in 1:group_k){
        #算出比例=個數/總數
        new=data.frame(c(sum(fit==k)/nrow(avg_complete)))
        colnames(new)=paste(i,j,sep="+")
        tmp=rbind(tmp,new)
        #============B第二個表作出圖用途 單筆 單筆的疊加
        new1=data.frame(values=c(sum(fit==k)/nrow(avg_complete)),G=paste("G",k),method=paste(substring(i,1,3),substring(j,1,3),sep="+"))
        dfB=rbind(dfB,new1)
      }
      dfA=cbind(dfA,tmp)
    }
  }
  #回傳沒有tuple可以用，只能放list 外面再用取list值的方法
  list_AB=list(dfA,dfB)
  return (list_AB)
}

# #==================BT_ggplot2出圖=========
# #第一種出圖方式效果很差，字變得模糊，應該是因為轉來轉去的關西
# # graph_SAVE_BT=function(group_number,df){
# #   png(filename=paste("BT_k=k",group_number,".png",sep = ""), width = 1300, height = 500)
# #   print(ggplot(df) +
# #     aes(x = method, fill = G, weight = values) +
# #     geom_bar() +
# #     scale_fill_hue() +
# #     labs(x = "Distance(群+點)", y = "Proportion比例", title = paste("階層式分群(bottom-top k=",group_number,")", sep=""), fill = "Group") +
# #     theme_solarized()+
# #     theme(legend.position = "right"))
# #   dev.off()
# # }
#第二種用GGPLOT2 原生出圖方式效果很好
graph_SAVE_BT=function(n,group_number,df){
                ggplot(df) +
                        aes(x = method, fill = G, weight = values) +
                        geom_bar() +
                        scale_fill_hue() +
                        labs(x = "Distance(群+點)", y = "Proportion比例", title = paste("階層式分群(bottom-top k=",group_number,")", sep=""), fill = "Group") +
                        theme_solarized()+
                        theme(legend.position = "right")
                ggsave(paste("BT_k=",group_number,"var",n,".png",sep = ""),width = 13, height = 6)
}

BT_group_2_6=function(data,n){
  df_all_min=data.frame()
  for(i in 2:6){
    tmp=BT_function(data,i)
    graph_SAVE_BT(n,i,tmp[[2]])
    #將分群數，最小值，最小值的名稱 存進DF
    df_min=data.frame(k=i,values=min(diag(var(tmp[[1]]))),text=names(which.min(diag(var(tmp[[1]])))))
    df_all_min=rbind(df_all_min,df_min)
  }
  ggplot(df_all_min) +
    aes(x = k, y = values, fill = text) +
    geom_tile(size = 1L) +
    scale_fill_brewer(palette = "Accent") +
    labs(x = "Groups群數", y = "VAR變異數值", title = "Minimal Variance and Groups", fill = "Distance(群+點)") +
    theme_foundation()
  ggsave(paste("BT_MIN","+var",n,".png",sep = ""),width = 13, height = 6)
}

BT_group_2_6(avg_complete[,-seq(from=1,to=19)],5)



#可選模型 指標 資料集
library(factoextra)
#有嘗試用"silhouette"的多種距離來找K 都是落在2
fviz_nbclust(avg_complete[,-seq(from=1,to=2)], 
             FUNcluster = hcut,  # hierarchical clustering
             method = "silhouette",     # "silhouette" "wss" "gap_stat" total within sum of square
             k.max = 8,       # max number of clusters to consider
             diss = dist(avg_complete[,-seq(from=1,to=2)], method = "euclidean")
             )
library(pamk)
library(randomForest)
library(fpc)
library(cluster)
#K-Medoid PAM方法  kmeans改良 抓實際點當中心
pamk.best <- pamk(avg_complete[,-seq(from=1,to=19)])
pamk.best$nc

#密度式分群
ds = dbscan(data = dist(avg_complete[,-seq(from=1,to=19)]),eps= 0.2, MinPts = 5, method="dist")
#隨機森林分群
a=randomForest(avg_complete[,-seq(from=1,to=19)])
a$classes

plot(ds, avg_complete23[,-seq(from=1,to=252)])

clusplot(pam(avg_complete23[,-seq(from=1,to=252)], pamk.best$nc))

#檢測指標
gap_stat <- clusGap(x = avg_complete[,-seq(from=1,to=19)],FUNcluster = hcut, nstart = 5, K.max = 8, B = 50)
fviz_gap_stat(gap_stat)

#kmeans 出圖
km.res <- kmeans(avg_complete[,-seq(from=1,to=19)],3)
fviz_cluster(km.res, data = avg_complete[,-seq(from=1,to=19)])


#廣義出圖方式
q =sapply(
  list(kmeans=km$cluster, 
       hc_single=hc_single, 
       hc_complete=hc_complete), function(c)cluster.stats(dist(customer_s),c)[c("within.cluster.ss","avg.silwidth")])
install.packages("largeVis")

