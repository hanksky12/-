### 遺失值處理(missing value)
setwd('~/R/riii')
load('./applenews.RData')
#隨機製造遺失值
idx= sample(1:nrow(applenews),size=30)#隨機抽30個樣本 返回index vector
applenews[idx,'clicked'] = NA #讓clicked欄位 變成NA值

##################對遺失值移除
#檢查每個欄位有無遺失值 
sapply(names(applenews),function(e){ sum(is.na(applenews[,e])) >0 })#BOOL轉數字去加 

#移除missing value       用is.na 對單欄位
is.na(applenews)# BOOL vector     #找尋遺失值
sum(is.na(applenews$clicked))
cleaned_data = applenews[!is.na(applenews$clicked),]#  !+布林向量 (T=>F F=>T)

#移除missing value     用complete.cases對整筆資料
complete.cases(applenews)         #找尋遺失值
cleaned_data2 = applenews[complete.cases(applenews),]


#############對遺失值以全體平均填補
load('./Statistics/applenews.RData')
applenews[idx,'clicked'] = NA

mean_clicked = round(mean(applenews$clicked,na.rm=T),0)##算平均裡面有na 會回傳na 後面參數na.rm=T去跳過
applenews$clicked[is.na(applenews$clicked)] = mean_clicked
#檢查遺失值 
sum(is.na(applenews$clicked))


#############對遺失值以類別平均填補
setwd('~/lecture/riii')
load('./Statistics/applenews.RData')
applenews[idx,'clicked'] = NA

tapply(applenews$clicked,applenews$category,mean)#直接用mean 會遇到<<<<NA返回的問題>>>>
cat_means = tapply(applenews$clicked,applenews$category,function(e){round(mean(e,na.rm=T),0)})
cat_means["3C"]
#對不同類別填入不同類平均
for(i in names(cat_means)){
  applenews[applenews$category == i & is.na(applenews$clicked),'clicked'] = cat_means[i]
}

sum(is.na(applenews$clicked))


################## mice套件 
##如果有百欄位 對其中一欄位我要用模型來填補 對每一個欄位有遺失都要醬做太累 
#install.packages('mice')
library(mice)
data(iris)
na_list = sample(1:nrow(iris),15)
iris[na_list,'Sepal.Length'] = NA
#常用cart 或rf 不用去d考慮y是數值或類別型
mice.data <- mice(data=iris,m = 3,method = "cart")#3次抽樣結果建模 回傳3個模型

complete(mice.data,1)#第一次建模結果

complete(mice.data,1)[na_list,'Sepal.Length']#返回原本是遺失值後來填補的結果
complete(mice.data,2)[na_list,'Sepal.Length']
complete(mice.data,3)[na_list,'Sepal.Length']

##比較各"""模型"""預測結果是否穩定(mean接近0,var很小)==>任何一組都可信
diff1 = complete(mice.data,1)[na_list,'Sepal.Length'] - complete(mice.data,2)[na_list,'Sepal.Length']

diff2 = complete(mice.data,1)[na_list,'Sepal.Length'] - complete(mice.data,3)[na_list,'Sepal.Length']

diff3 = complete(mice.data,2)[na_list,'Sepal.Length'] - complete(mice.data,3)[na_list,'Sepal.Length']

mean(c(diff1,diff2,diff3))
var(c(diff1,diff2,diff3))

complete(mice.data,1)

#################dplyr套件
#類似SQL的資料操作
#install.packages("dplyr")
library(dplyr)
load('./applenews.RData')
str(applenews)
applenews=applenews[,-1]

#過濾功能
#R
applenews[applenews$category=="娛樂",]
#dplyr
filter(applenews,category=="娛樂")

#欄位選取
#R
applenews[,c("category","clicked")]
#dplyr
select(applenews,category,clicked)

#鏈結chaining
#%>% 類似linux的pipe  參數的第一個預設都承接前面  可以提出來不用寫
applenews %>%
  select(.,category,clicked) %>%
  filter(category=="娛樂") %>%
  head()

###############select
#列舉式 欄位
head(select(applenews,category,clicked))
#區間式 欄位(range)
head(select(applenews,title:dt,category:clicked))
#selected helpers 欄位   (命名時，要注意命名的相關性)
#contains() starts_with() ends_with() matches(): Matches a regular expression
head(select(applenews,contains('click')))
head(select(iris,starts_with("Sepal")))
head(select(iris,ends_with("Length")))

###########group_by & summarize
###單欄位
applenews %>%
  group_by(category) %>%
  summarise(clicked_mean = mean(clicked, na.rm=TRUE)) %>%
  arrange(desc(clicked_mean))

###多欄位&多運算
applenews %>%
  group_by(category) %>%
  summarise_at(.vars =vars(clicked),.funs = funs(sum,mean,min,max,sd))

###############連接資料庫(mysql)
#資料庫driver   Mysql 8.0版  Rmysql沒有繼續開發(R作者沒有繼續開發)  RMariaDB(底層連線式相似的)

## alter mysql 8.0 password encryption 因為R沒跟上8.0的加密 所以要到MySQL 去執行code
#https://stackoverflow.com/questions/49194719/authentication-plugin-caching-sha2-password-cannot-be-loaded
##ALTER USER 'yourusername'@'localhost' IDENTIFIED WITH mysql_native_password BY 'youpassword';
#CREATE DATABASE test CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
#console login 在console下指令前
#mysql -u USERNAME -p PASSWORD -h HOSTNAMEORIP DATABASENAME
install.packages("RMariaDB")
library(RMariaDB)
#dbplyr:A 'dplyr' Back End for Databases
install.packages('dbplyr')
library(dbplyr)

data("iris")
##iris example
#建立連線(一次只會跟一個DB連線)
conn = dbConnect(MariaDB(),dbname='mydb',host='127.0.0.1',port=3306,user='root',password='mindyiloveyou')
#刪資料裡面的表
db_drop_table(conn,'iris')
#df送進mysql創造table
copy_to(conn,iris,temporary = F)#temporary=F ==> 執行+commit
#連線到table iris
#在collect之前   Source:table<iris> [?? x 5] 還沒被執行 先回傳預覽  不知幾列*5欄
tbl(conn,"iris") %>%
  select(starts_with('Sepal'),'Species') %>%
  group_by(Species) %>%
  summarise_at(.funs=funs(mean(.,na.rm=T),sd(.,na.rm=T)),.vars=vars(starts_with('Sepal'))) %>%
  collect()#等於SQL的commit 才真正抓DATA
#DBI查詢
#dbGetQueryc函數   (將SQL指令傳入DB抓資料,直接commit,不如直接開SQL操作)
dbGetQuery(conn,'select * from iris') %>% filter(Species == 'setosa')
dbGetQuery(conn,'select `Sepal.Length` from iris') # `` 波浪符號不加shift

dbListTables(conn)


#############機器學習
#決策樹
#C50
library(C50)
data(churn)
str(churnTrain)

#篩選要的欄位
#第一種 churnTrain[,c()]
#第二種 dplyr
#第三種 %in% 檢查後面元素有沒有出現在前面的元素   %*% %>% %in%
names(churnTrain) %in%  c("state","area_code","account_length" ) #返回BOOL VECTOR 
!names(churnTrain) %in%  c("state","area_code","account_length" )
#選擇建模變數
variable.list=!names(churnTrain) %in%  c("state","area_code","account_length" )
churnTrain=churnTrain[,variable.list]
churnTest=churnTest[,variable.list]

#訓練集跟測試集比例7:3 8:2 9:1 
#sample
sample(1:10)
sample(1:10,size = 5) #size 抽幾次
sample(c(0,1),size = 10,replace = T) #replace=T取後放回
sample(c(0,1),size = 10,replace = T,prob=c(0.7,0.3)) #抽樣的比例
sample.int(20,12)#兩個參數都要放整數，這個例子是1:20中的12個不重複樣本

set.seed(2)#把隨機種子序暫時固定(整數在2+-31次方)==>用在每次抽樣前去呼叫才會有固定的抽樣結果   (R裡面跟隨機有關的 都有種子序)
#把資料分成 訓練集 和測試集 (練習而已，這邊早就分好了)
ind=sample(1:2,size=nrow(churnTrain),replace = T,prob = c(0.7,0.3))
table(ind)#看一下
trainset=churnTrain[ind==1,]
testset=churnTrain[ind==2,]

####cart
library(rpart)
##############事前修剪
#怕Overfit   minsplit少於20個樣本就不往下分(太大underfit)   cp值=>懲罰項=>成本複雜度  小於0.01不分裂
con=rpart.control(minsplit = 20,cp=0.001) 
#建模
churn.rp=rpart(churn~.,data = trainset,control = con)
#檢查模型報告
#可以知道特徵值重要性
s=summary(churn.rp) 
s$cptable #把模型存入變數 就可以用$下選單來用他

#########畫決策樹
#內建畫圖
par(mfrow=c(1,1))
?plot.rpart
#margin 離邊框距離
#branch 給樹支ㄧ些角度
#cex字體大小
#all=T 每個節點都有類別的預測
#use.n=T 節點樣本分布比例 ==>前面YES樣本個數/後面NO樣本個數
plot(churn.rp, uniform=TRUE,branch = 0.6, margin=0.1)
text(churn.rp, all=TRUE, use.n=TRUE, cex=0.7)

#套件畫圖
#install.packages("rpart.plot")
library(rpart.plot)
rpart.plot(churn.rp)

############事後修剪 
#找出minimum cross-validation errors
min_row=which.min(churn.rp$cptable[,"xerror"])
churn.cp=churn.rp$cptable[min_row,"CP"]
#用prune函數   將churn.cp設為臨界值來修剪樹
prune.tree=prune(churn.rp, cp=churn.cp)
plot(prune.tree, uniform=TRUE,branch = 0.6, margin=0.1)
text(prune.tree, all=TRUE, use.n=TRUE, cex=0.7)

test_tree = prune(churn.rp,cp=0.06)
plot(test_tree, margin=0.1)
text(test_tree, all=TRUE, use.n=TRUE, cex=0.7)

#預測函數predict   預測的Y
predictions=predict(prune_tree,testset)
predictions=predict(prune_tree,testset,type="class")#機率超過0.5預測為該類  不加class 預設回傳機率
#取出測試集       真實的Y
predictions==testset$churn
#混淆矩陣
library("caret")
library("e1071")
confusionMatrix(table(predictions,testset$churn)) #預測在前 真實在後 不然做起來會反
