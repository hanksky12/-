#P147 餘弦相似度
x <- c(1,2,3,5,8)
y <- c(0.11,0.12,0.13,0.15,0.18)
a <- matrix(c(x,y),c(5,2))#直的放
a
cos_xy=(a[,1]%*%a[,2])/(sum(a[,1]^2)^0.5*sum(a[,2]^2)^0.5)#自動轉向
cos_xy                        

cos_xy=(x%*%y)/(sum(x^2)^0.5*sum(y^2)^0.5)#也可以直接做
cos_xy
cor(a[,1],a[,2])
#P152交叉統計表    ftable
z <- data.frame(Main= c('豚','牛','牛','牛','豚','牛','豚'), sub=c('有','沒有','沒有','有','有','有','沒有') , drink=c('tea','coffee','coffee','tea','coffee','tea','coffee'))
z
ftable(z,row.vars = 1:2,col.vars = "drink")
ftable(z,row.vars = "Main",col.vars = 2:3)

###plyr套件  提供樞紐分析表(excel)需要的資料,不用每次都給一份
install.packages("plyr") 
library(plyr)
df<- data.frame( group = c(rep('個人戶', 20), rep('企業戶', 20)), sex = sample(c("M", "F"), size = 40, replace = TRUE), age = floor(runif(n = 40, min = 25, max = 40)), bill = floor(runif(n = 40, min = 199, max = 2600)) )
## 利用group, sex進行分組，並計算年齡的平均數、標準差以及bill總和與平均 
ddply(df, .(group, sex), summarize, mean_age = round(mean(age), 2), sd_age = round(sd(age), 2), sum_bill = sum(bill), mean_bill = round(mean(bill), 2) )
#計算資料筆數count
ddply(df, c('group','sex'), nrow) 
ddply(df, c('group','sex','age'), nrow) #是不是很像樞紐分析表的原始資料

##################用vcd計算列聯表百分比
install.packages("vcd") 
library(vcd)
#隨機資料40筆
df<- data.frame( group = c(rep('個人戶', 20), rep('企業戶', 20)), sex = sample(c("M", "F"), size = 40, replace = TRUE), age = floor(runif(n = 40, min = 25, max = 40)), bill = floor(runif(n = 40, min = 199, max = 2600)) )
df
prop.table(df$bill) 
data.frame(df$bill,prop.table(df$bill))
table(df$age)
prop.table( table(df$age) )
table(df$age, df$group)

prop.table(table(df$age, df$group) )     #    無參數全部相加 = 1
prop.table(table(df$age, df$group) ,1)   # 參數1表示各列加總 = 1
prop.table(table(df$age, df$group) ,2 )  # 參數2表示各行加總 = 1

#散佈圖
data(iris) 
iris
attach(iris) #少打iris$ 就可以呼叫欄位
plot(Petal.Length~Petal.Width, col=Species) #散佈圖指令

#P158 長條圖
data(mtcars) 
attach(mtcars)
table(cyl) #利用汽缸數產生次數分配
#直，絕對數字
T_cyl=table(cyl)
barplot(T_cyl,main = "汽缸數次數分配表",xlab="汽缸數",col=c("red","blue","green"),names.arg=c("四汽缸","六汽缸","八汽缸"),border="cyan")
#橫，相對數字(百分比)，y加名稱
library(vcd)
T_cyl=prop.table(table(cyl))
barplot(T_cyl,main = "汽缸數次數分配表",xlab="汽缸數",ylab="百分比",col=c("red","blue","green"),names.arg=c("四汽缸","六汽缸","八汽缸"),border="cyan",horiz=T)
#分組長條圖  想看4.6.8汽缸下 手自排比例
T_cyl2 = table(am,cyl) #建立變速器與汽缸數交叉表   am放前面
T_cyl2 
# legend 是圖例 # beside是分組圖還是堆疊
barplot(T_cyl2 , main="cyl 汽缸數次數分配表", xlab="汽缸數", col=c("red", "blue"), names.arg=c("4 汽缸", "6 汽缸", "8 汽缸"), border = "cyan", horiz=FALSE, legend = rownames(T_cyl2), beside=TRUE)
barplot(T_cyl2 , main="cyl 汽缸數次數分配表", xlab="汽缸數", col=c("red", "blue"), names.arg=c("4 汽缸", "6 汽缸", "8 汽缸"), border = "cyan", horiz=FALSE, legend = rownames(T_cyl2), beside=F,args.legend = list(x = "topleft"),legend.text = c("自排", "手排"))#這個比較好看比例
##### 長條圖(百分比堆疊圖)
prop.table( table(am,cyl) ,2)#行加起來=1 百分比呈現
T_cyl3 = prop.table( table(am,cyl) ,2)
par(las=1)##標籤=1，表示標籤文字為水平。標籤=2，表示標籤文字為垂直
#space=2 表示直條間的距離
#cex.names=2 表示標籤文字大小為原來的兩倍
barplot(T_cyl3 , main="cyl 汽缸數次數百分比堆疊圖", xlab="汽缸數", col=c("red", "blue"), names.arg=c("4 汽缸", "6 汽缸", "8 汽缸"), border = "cyan", horiz=FALSE, legend = c('自動','手動'), beside=FALSE, cex.names=2,space=2)


#####直方圖 p162
install.packages("C50")
library(C50)
data(churn)
attach(churnTrain)
str(churnTrain)
par(mfrow=c(2,2))#圖片區配置 2*2 的圖，共4個圖 要取消設回(1,1)
#設定分組組數
hist(total_day_minutes, xlab=" 白天通話分鐘數", main="breaks =11", ylab="門號數", col="red" ) # 參數breaks預設為11 
hist(total_day_minutes, xlab=" 白天通話分鐘數", main="breaks =2", ylab="門號數", col="red", breaks=2 ) # 參數breaks設為2 
hist(total_day_minutes, xlab=" 白天通話分鐘數", main="breaks =20", ylab="門號數", col="red", breaks=20 ) # 參數breaks設為20 
hist(total_day_minutes, xlab=" 白天通話分鐘數", main="breaks =7", ylab="門號數", col="red", breaks=7 ) # 參數breaks設為7

#########盒鬚圖 P168
dt=data.frame(total_eve_minutes,total_night_minutes,total_day_minutes)
#顯示白天、晚上、半夜通話分鐘數
boxplot(dt,horizontal = F,xlab="通話分鐘數",col=terrain.colors(3))
legend("topright",title="撥打分鐘數",c("eve","night","day"),fill=terrain.colors(3),horiz=F,ncol=1,cex=0.8)
#檢視在不同地區流失客戶與未流失客戶的晚上通話時間分布
boxplot(total_eve_minutes~area_code*churn,horizontal=FALSE, xlab="夜晚通話分鐘數",col=terrain.colors(3))

#tree map
install.packages('treemap')
library(treemap)
x <- read.table(file.choose(),header=T, sep=",", fileEncoding='big5') #選擇TaiwanGov.csv 
treemap(x,index=c('縣市'),vSize='面積',vColor='面積')
treemap(x,index=c('縣市','行政區名稱'),vSize='面積',vColor='面積')
treemap(x,index=c('縣市','行政區名稱'),vSize='人口數',vColor='人口數')
new_x=transform(x,人口密度=x$人口數/x$面積)
treemap(new_x,index=c('縣市','行政區名稱'),vSize='人口密度',vColor='人口密度')
#簡單迴歸模型 P205
# 自行產生藥劑量與感冒痊癒天數資料 
med <- c(3,3,4,3,6,8,8,9) #藥劑量 
day <- c(22,25,18,20,16,9,12,5)#感冒痊癒天
New_x<- data.frame(x=5)#預測當x=5時的痊癒天數

# 建立一個簡單線性迴歸模型 
Train <- data.frame(x = med, y = day) #訓練樣本
lmTrain<- lm(formula = y ~ x, data = Train) #建模 LM
predicted <- predict(lmTrain , newdata= New_x)# 測試樣本  預測當x=5時的痊癒天數
predicted#17.1413 
# 模型摘要  
summary(lmTrain)

#多元迴歸 P207
# 自行產生藥劑量、平均每日睡眠時間與感冒痊癒天數資料 
x1 <- c(3,3,4,3,6,8,8,9) #藥劑量
x2 <- c(3,1,6,4,9,10,8,11) #平均每日睡眠時數 
y <- c(22,25,18,20,16,9,12,5) #感冒痊癒天數
#新患者資料
New_x1 <- 5 #預測當x=5時的痊癒天數 
New_x2 <- 7 #每日睡眠時數 
New_data<- data.frame(x1 = 5, x2=7)
# 建立一個線性迴歸模型 
Train<- data.frame(x1 = x1, x2=x2, y = y) 
lmTrain <- lm(formula = y ~., data = Train)
#預測新患者感冒痊癒天數
predicted <- predict(lmTrain , newdata= New_data) 
predicted 
# 模型摘要 
summary(lmTrain)

##############新生兒資料 <cart分類回歸> <製作訓練與測試樣本>  <MAPE指標>    P209
babyData <- read.table(file.choose(),header=T, sep=",")
#排除有遺漏值的資料列
babyData=na.exclude(babyData)

########訓練樣本70%與測試樣本30% 
n=0.3*nrow(babyData) 
test.index=sample(1:nrow(babyData),n)
Train=babyData[-test.index,] 
Test=babyData[test.index,]

##############確認訓練樣本與測試樣本分佈一致 
par(mfrow=c(1,2)) #分兩圖
hist(Train$bwt) 
hist(Test$bwt)

#建模 
install.packages("rpart") 
library(rpart) 
baby.tree=rpart(bwt~. ,data=Train)# 使用CART分類回歸樹演算法
baby.tree 
plot(baby.tree) #畫圖只是讓我們了解
text(baby.tree, cex=.8)

#variable importance 
baby.tree$variable.importance  #####選x變數
# MAPE of train and test group
#訓練樣本的MAPE
y=babyData$bwt[-test.index] 
y_hat=predict(baby.tree,newdata=Train, type="vector") 
train.MAPE=mean(abs(y-y_hat)/y) 
cat("MAPE(train)=",train.MAPE*100,"%\n")
##測試樣本的MAPE
y=babyData$bwt[test.index] 
y_hat=predict(baby.tree,newdata=Test, type="vector") #返回的y 不是純量，是vector
test.MAPE=mean(abs(y-y_hat)/y) 
cat("MAPE(test)=",test.MAPE*100,"%\n")

##HW 以多元回歸建模新生兒資料P211
babyData <- read.table(file.choose(),header=T, sep=",")
babyData=na.exclude(babyData)
str(babyData)#1174
#分7:3
n=0.3*nrow(babyData) #352.2
test.index=sample(1:nrow(babyData),n)
Train_baby=babyData[-test.index,]#822
Test_baby=babyData[test.index,]#352
#分兩圖 看分佈
par(mfrow=c(1,2)) 
hist(Train_baby$bwt) 
hist(Test_baby$bwt)
#建模
lmTrain=lm(formula = bwt ~.-age, data = Train_baby)# 0.2347 
summary(lmTrain)
lmTrain=lm(formula = bwt ~.-age-weight, data = Train_baby)#0.2356 
#mape  train
y=Train_baby$bwt
y_hat=predict(lmTrain,newdata=Train_baby, type="response") 
mape=mean(abs(y-y_hat)/y)
cat("mape_train=",mape*100,"%")#mape_train= 11.15818 %
#mape test
y2=Test_baby$bwt
y2_hat=predict(lmTrain,newdata=Test_baby, type="response") 
mape2=mean(abs(y2-y2_hat)/y2)
cat("mape_test=",mape2*100,"%")#mape_test= 10.18286 %
