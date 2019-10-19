#http://mlwiki.org/index.php/Cost-Complexity_Pruning
############### caret package  (常用的演算法都在套件裡面)
#install.packages("caret")
library(caret)
library(C50)
data(churn)
names(churnTrain) %in% c("state", "area_code", "account_length")
!names(churnTrain) %in% c("state", "area_code", "account_length")
#選擇建模變數
variable.list = !names(churnTrain) %in% c('state','area_code','account_length')
churnTrain=churnTrain[,variable.list]
churnTest=churnTest[,variable.list]
#method=cv  ==>K-fold cross-valid ==> 參數number=K  =>建模10次     
#method=repeatedcv ==> 參數多寫repeats 整個cv重複3次==>建模30次(一旦被分割成10分，每份內的資料是固定，這邊可做到重新抽樣三次效果再分割的效果)
control=trainControl(method="repeatedcv", number=10, repeats=3)
#建模函數
model =train(churn~., data=churnTrain, method="rpart", trControl=control)##method決定你想要的演算法

predictions = predict(model,churnTest)
table(predictions,churnTest$churn)
confusionMatrix(table(predictions,churnTest$churn))#混淆矩陣

### caret 套件使用說明
# 查詢caret package 有實作的所有演算法 238個 監督式都有
names(getModelInfo())
# 查詢caret package 有沒有實作rpart演算法
names(getModelInfo())[grep('rpart',names(getModelInfo()))] #0926  grep找字
# 查詢rpart model資訊
getModelInfo('rpart')
getModelInfo('rf')
#$type 可用在哪種資料 $library 套件名稱

# 查詢rpart model可以tune的parameters
getModelInfo('rpart')$rpart
getModelInfo('rpart')$rpart$parameters


################### caret tune  調參+出報表+選標準
#summaryFunction報表評分標準  
#twoClassSummary ROC曲線=>classProbs=T（因为train函数默认并不计算概率） multiClassSummary:AUC、F1、ACC..  prSummary:AUC,Precision,Recall
control=trainControl(method="repeatedcv", number=10, repeats=3,summaryFunction = prSummary,classProbs=T)
#調參數要放vector==>回傳各參數對應的模型   (可調哪些參數去看getModelInfo('rpart')$rpart$parameters)  
tune_funs = expand.grid(cp=seq(0,0.1,0.01))

#建模
#metric 最後選擇模型的評分標準 
model =train(churn~., data=churnTrain, method="rpart", trControl=control,tuneGrid=tune_funs,metric="AUC")

model  #回傳參數最佳的選擇(rpart==>cp值)
predictions = predict(model, churnTest)
confusionMatrix(table(predictions,churnTest$churn))

### 找重要變數
importance = varImp(model, scale=T)#scale 正規化到0-100 不開沒差
importance
plot(importance)


########ROC曲線
#https://www.youtube.com/watch?v=OAl6eAyP-yo
#http://www.navan.name/roc/
#考慮到切分點只能在機率0.5嗎? 讓切分點當閥值去移動畫出ROC曲線
library(ROCR)
predictions=predict(model,churnTest,type="prob") 
head(predictions)
########第一步 取出測試集中YES的機率
pred.to.roc=predictions[,"yes"] 
pred.rocr=prediction(pred.to.roc,churnTest$churn)
pred.rocr
#只有單獨計算==> measure
auc_value<-performance(pred.rocr, measure ="auc")
(AUC=auc_value@y.values )#舊版R取東西用@  現在都是$

######第二步 ===>measure=>Y軸 x.measure=>X軸 
#可畫的圖 ROC curves,Precision/recall graphs,Sensitivity/specificity plots,Lift charts
perf.tpr.rocr<-performance(pred.rocr, measure="tpr",x.measure = "fpr")
plot(perf.tpr.rocr,main=paste("AUC:",(auc_value@y.values)))


###########集成學習(多個模型一起做預測或分類)
#Bagging概念:是將樣本重複抽樣(取後放回)，產生多個子集(Subsets)後，建立多個模型，再將所有模型的結果彙整。預測問題(Regression Problem)=>平均(Average)；分類問題(Classification Problem)=>投票法(Voting)，可降低variance
#boosting概念:使用弱模型，前一個模型對樣本預測錯誤以後，把分錯的權重加大，依序往下一個模型重新分類，最後可降低bias
#Stacking概念:把本來的預測結果再進一步做預測

###########隨機森林 (Bagging)
#http://www.rpubs.com/skydome20/R-Note16-Ensemble_Learning
library(randomForest)
library('caret')
library('e1071')
library(ROCR)
#先用預設建模
rf_model = randomForest(formula=churn ~ .,data=churnTrain)

#找最佳棵樹 (看誤差)
plot(rf_model)#ntree大概從50棵樹 之後就平穩 預設500棵
legend("topright",colnames(rf_model$err.rate),col=1:3,cex=0.8,fill=1:3)#黑色是整體誤差 紅色是YES樣本的誤差 綠色是NO樣本
#find nest mtry   (挑變數個數)
tuneRF(churnTrain[,-17],churnTrain[,17])#mtry 特徵值個數 預設 取大概原本1/3當樹的特徵 後面放要預測的欄位
#重新調整再建模
rf_model <- randomForest(churn ~., data = churnTrain, ntree=50,mtry=4)
#用caret packager建RF   rf_model = train(churn~.,data=churnTrain,method='rf')

confusionMatrix(table(predict(rf_model,churnTest),churnTest$churn))
#畫圖ROC 算AUC
rf.predict.prob <- predict(rf_model, churnTest, type="prob")
rf.prediction <- prediction(rf.predict.prob[,"yes"], as.factor(churnTest$churn))
rf.auc <- performance(rf.prediction, measure = "auc")
rf.performance <- performance(rf.prediction, measure="tpr",x.measure="fpr")
plot(rf.performance)
########用ROC曲線比較CART 和 RF
tune_funs = expand.grid(cp=seq(0,0.1,0.01))
rpart_model =train(churn~., data=churnTrain, method="rpart",tuneGrid=tune_funs)

rpart_prob_yes = predict(rpart_model,churnTest,type='prob')[,1]
rpart_pred.rocr = prediction(rpart_prob_yes,churnTest$churn)
rpart_perf.rocr = performance(rpart_pred.rocr,measure = 'tpr',x.measure = 'fpr')

plot(rpart_perf.rocr,col='red')
plot(rf.performance,col='black',add=T)#add=T 將後面的圖疊加在前面的圖
legend(x=0.7, y=0.2, legend =c('randomforest','rpart'), fill= c("black","red"))#加個圖例


#############非監督式學習    
#數值型:點跟點=>用距離公式
#文字型:文章跟文章間的相似度=>向量跟向量的距離=>用cosθ
#影像型:圖片與圖片的相似度=>三維矩陣與三維矩陣的距離

#分群模型
#距離計算  點跟點 (數值型)
x=c(0,0,1,1,1,1)
y=c(1,0,1,1,0,1)

#euclidean
rbind(x,y)
dist(rbind(x,y),method = "euclidean")#距離公式自選

#city block
dist(rbind(x,y), method ="manhattan")

z=c(1,1,1,0,1,1)
rbind(x,y,z)
dist(rbind(x,y,z),method = "euclidean")
dist(rbind(x,y,z),method = "manhattan")


#階層式分群
#聚合式(bottom-up)
setwd('F:/資策會/R/teacher/riii/data')
customer=read.csv('./customer.csv',header=TRUE)
head(customer)
str(customer)

#數值變數作正規化  =>將資料去掉單位(避免單位影響)
#scale函數  Z-score 離平均數幾個標準差  不同欄位各別計算 大家的單位都變成標準差
customer_s =scale(customer[,-1])
?scale

#正規化後的變數平均為0 標準差為1
#定義離群值:三個標準差之外  (能簡單找出)
round(mean(customer_s[,3]),3)#以性別舉例
round(sd(customer_s[,3]),3)

######階層式分群(bottom-up)
#第一個method 算點跟點的距離 第二個method 算群跟群的距離 

?hclust
hc=hclust(dist(customer_s, method="euclidean"), method="ward.D2")
plot(hc,hang =-0.01, cex=0.7)

hc3 =hclust(dist(customer, method="euclidean"), method="single")
plot(hc3, hang =-0.01, cex=0.8)


############cuttree
#k 想分群的組數
fit =cutree(hc, k =4)
fit
#在圖形上畫出分群線
#border 線的顏色
table(fit)
plot(hc, hang =-0.01, cex=0.7)#hang樹枝從哪裡開始長(看起來齊頭==>不重要)
rect.hclust(hc, k =4, border="red")
rect.hclust(hc, k =3, border="blue")

#把同群的樣本抓出來
#回原始資料找 才能看出更多資料
#代表這群人   中心點的資訊
#如何定義 就是市場人員的專業了
c_1=customer[fit==1,]#fit整數向量
summary(c_1)
c_2=customer[fit==2,]
summary(c_2)
c_3=customer[fit==3,]
summary(c_3)
c_4=customer[fit==4,]
summary(c_4)

#########階層式分群(top-down)
library(cluster)
?diana
dv =diana(customer_s, metric ="euclidean")
summary(dv)
plot(dv)

fit2 =cutree(dv,k=4)
c_1 = customer[fit2 ==2,]
summary(c_1)



##########K-means
#centers 決定幾群``
str(customer_s)
set.seed(22)
fit =kmeans(customer_s, centers=4)
?kmeans

#fit$cluster#分組結果
#fit$centers#群中心位置  row 組別 col 特徵
#t()轉置
#beside=T 以dodge 排列
barplot(t(fit$centers), beside =TRUE,xlab="cluster", ylab="value")
?barplot
fit$centers
#一樣可以去抓原始資料 用SUMMARY看
customer[fit$cluster == 1,]

######投影到二維空間，繪製分群結果  (降維)
#通常很難用視覺化去呈現每種特徵
plot(customer[,-1],col=fit$cluster)#從圖裡面找不到完美的將四群分開的圖
#降維 不一定要做 但可以嘗試模型效果有沒有更好
#將4維降至2維 投影必失真(損失資訊)  但差不多
#clusplot投影函數  (背後用PCA) 
library(cluster)
clusplot(customer_s, fit$cluster, color=TRUE, shade=TRUE) #用這兩個主成分 完美分開 四個群 這邊資訊量剩85趴 
 
#主成分分析法component  DM教過
pca=princomp(customer_s)#Cumulative Proportion 看累積資訊量
summary(pca)
pca$loadings #看原本欄位權重 組成新主成分

################尋找K-means  的最佳K值
#介紹silhouette   對每個樣本點都個別計算
library('cluster')
par(mfrow= c(1,1))
set.seed(22)
km =kmeans(customer_s, 4)
#參數 :分群的結果 與距離矩陣
kms=silhouette(km$cluster,dist(customer_s))#看課本 值越大越好
summary(kms)
summary(kms)$avg.width#全部的平均
plot(kms)             #第幾群:群內個數|該群的平均


nk=2:10
############第一種silhouette
#迴圈 K從2~10 算SW值
SW = sapply(nk,function(k){
  set.seed(22); summary(silhouette(kmeans(customer_s,centers=k),dist(customer_s)))$avg.width
})

#畫圖==>找高點
plot(x=nk,y=SW,type='l')

###########第二種WSS (組內距離)
#看DM  原本k-means 報表裡面有指標 一定會隨著K越多值越小 
WSS =sapply(nk, function(k){set.seed(22);kmeans(customer_s, centers=k)$tot.withinss})
WSS
#畫圖==>看斜率找反曲點
plot(x=nk, y=WSS, type="l", xlab="number of k", ylab="within sum of squares")

#######################多模型  用WSS跟SW指標 同時比較
#可用在階層式 密度式 分裂式
##分群結果的統計
#install.packages("fpc")
library(fpc)
#先建三種模型
single_c=hclust(dist(customer_s), method="single")
hc_single=cutree(single_c, k =4)

complete_c=hclust(dist(customer_s), method="complete")
hc_complete=cutree(complete_c, k =4)

set.seed(22)
km =kmeans(customer_s, 4)
# 距離矩陣 分組結果向量
cs=cluster.stats(dist(customer_s),km$cluster)
cs[c("within.cluster.ss","avg.silwidth")]#WSS SW

q =sapply(
  list(kmeans=km$cluster, 
       hc_single=hc_single, 
       hc_complete=hc_complete), function(c)cluster.stats(dist(customer_s),c)[c("within.cluster.ss","avg.silwidth")])
q

########密度式分群
#DBSCAN

#製造隨機點
library(mlbench)
#install.packages("fpc")
library(fpc)
 
set.seed(500)
p = mlbench.cassini(500)
plot(p$x)

?mlbench.cassini
#指定Eps 跟 MinPts   (分群數無法指定)
#data可帶 method=dist距離矩陣 或   raw原始資料 
ds = dbscan(data = dist(p$x),eps= 0.2, MinPts = 2, method="dist")
ds
plot(ds, p$x)
#filter群集的raw data
cluster_1_raw = p$x[ds$cluster == 1,]
cluster_1_raw
#10/21周一公布   email name班級跟姓名 york@largitdata.com   副檔名db104_name_finalhw.Rmd