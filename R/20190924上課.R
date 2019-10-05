#DATA Frame
dat=c("mon","tue","wed","thu","fri")
age=c(28,26,34,12,22)
df
df=data.frame(dat,age)
class(df)
str(df)
summary(df)
data() 
data(iris)#指定資料集名稱
class(iris)
summary(iris)
str(iris)
head(iris)
#選尾巴
tail(iris)
tail(iris,10)
#[]篩選 放index,element name,condition
#用col name篩
iris[1:3,"Sepal.Length"]  #跟matrix一樣
iris[,"Species"]=="setosa"  #出來BOOL向量  品種是setosa
#用條件篩
iris[iris[,"Species"]=="setosa",]
iris[iris[,"Sepal.Length"]>5,] #花萼長度大於5的列
iris$Species=="setosa"  #等於19行
iris[iris$Species=="setosa",]
#join
df1=data.frame(cust_id=c(1:6),pro=c(rep("巧克力",3),rep("香蕉",3)))
df2=data.frame(cust_id=c(1:3),name=c("小王","小名","老王"))
#Inner join:
merge(x = df1, y= df2, by="cust_id")
#Outer join: 
merge(x = df1, y = df2, by = "cust_id", all = TRUE)
#Left outer: 
merge(x = df1, y = df2, by = "cust_id", all.x = TRUE)
#Right outer: 
merge(x = df1, y = df2, by = "cust_id", all.y = TRUE)
#Cross join: 
merge(x = df1, y = df2, by = NULL)
#用which做篩選
which(iris$Species=="setosa")
c(4,5,6)
max(c(4,5,6))#找最大值
which.max(c(4,5,6))#找最大值  的位置
#排序    #預設FALSE 升冪
#sort
head(iris)
sort(iris$Sepal.Length,decreasing = TRUE) #回傳排完的值
#order
order(iris$Sepal.Length) #回傳排完的index
iris[order(iris$Sepal.Length,decreasing = TRUE) ,]
#2017整年台積電 riii/data/2230.csv
getwd()#確認工作環境
setwd("E:/BIG\ DATA下載/R/riii/data") #斜線方向要改
#可到右邊手動到目錄資料夾,用MORE裡面的 set as working dire....
getwd()
tw2330=read.csv("E:/BIG\ DATA下載/R/riii/data/2330.csv",header=T)#絕對路徑 ,讀欄位名稱 預設是TRUE
str(tw2330)
tail(tw2330)
read.csv("./2330.csv",header=T) #相對路徑
########as 可以做型態轉換
as.character(c(1,2,3))
as.numeric(c(T,F,T))
c("low","high")
class(c("low","high"))
as.factor(c("low","high"))
tw2330$Date=as.Date(tw2330$ Date)#Fator 轉DATE  在塞回去取代原本那一行
class(as.Date(tw2330$ Date))  #日期的值越接近現在越大
str(tw2330)
#台積電 P35
tw2330$Date>="2017-01-01"
tw2230_2017=tw2330[tw2330$Date>="2017-01-01"&tw2330$Date<"2018-01-01",]
max(tw2230_2017$Close)# 直接取最高
tw2230_2017[order(tw2230_2017$Close,decreasing = TRUE),] 
#Lists
item=list(thing="hot",size=8)
item$thing #用$+KEY  抓value
flower=list(title="iris",data=iris)#想塞data frame也可
flower$data
class(flower$data)
#沒有KEY的list
li=list(c(1,2),c(3,4))
li[[1]] #用[[]] 抓 value
li[[2]]
#寫入資料 這兩種方法對大檔讀寫太慢
write.csv(tw2230_2017,file = "./tw2230_2017.csv")
write.table(tw2230_2017,file = "./tw2230_2017.txt",sep="@")
#readr套件  CSV 原本10倍以上的讀取 
install.packages("tidyverse")#裡面有8個套件readr,ggplot2....
install.packages("readr")
library("tidyverse") #跟py import依樣
tt2330=read_csv("E:/BIG\ DATA下載/R/riii/data/2330.csv",
                col_names=T,
                 col_types = cols(
                    Date = col_date(format = ""),
                    Open = col_double(),
                    High = col_double(),
                    Low = col_double(),
                    Close = col_double(),
                    Volume = col_double()
                  ))
#用參數colnames預設是T,參數col_types可改欄位的type
tt2330
#read excel  套件
install.packages("readxl")
library(readxl)
FinancialReport=read_excel("E:/BIG\ DATA下載/R/riii/data/FinancialReport.xlsx")
class(FinancialReport)  #tibble包起來
#read json
library(jsonlite)
json_data<- fromJSON('./rent.json')
json_data <- as_tibble(json_data) 
head(json_data)
#read XML
install.packages("XML")
library(XML)
url = 'http://opendata.epa.gov.tw/ws/Data/ATM00698/?$format=xml'
weather <- xmlToDataFrame(url)
View(weather)
str(weather)
#weather[ weather$SiteName == '臺北',  c('DataCreationDate','Temperature')   ]
#流程控制 if else 跟ifelse函數
x=5
if (x>3){
  print("x>3")}else{
  print("x<=3")}
if (x>3) print("x>3") else print("x<=3")
ifelse(x>3,"x>3","x<=3") #函數ifelse 條件 if T=do1 F=do2  
data(iris)
str(iris)
#對$Species做判斷 之後 改成factor 再放回原表當新欄位
iris$new_species=factor(ifelse(iris$Species=="setosa","issetosa","notsetosa"))
str(iris)
#for迴圈
for(i in 1:10){print(i)}
#1層
sum=0
for(i in 1:100) {sum=sum+i}
sum
#2層
fomat=matrix(1:9,byrow = T,nrow=3)
for (i in 1:nrow(mat)) {
  for (j in 1:ncol(mat)) {
    print(mat[i,j])
    
  }
  
}
#while
sum=0
cnt=0
while(cnt<=100){
  sum=sum+cnt
  cnt=cnt+1
}
sum
######練習9*9
#用迴圈
x=c()
for (i in 1:9) {
  for (j in 1:9) {
            x=c(x,c(i*j))
  }
  
}
mat4=matrix(x,byrow=T,nrow=9)
mat4
#用矩陣
mat1=matrix(1:9,byrow = T,nrow = 1)
mat2=matrix(1:9,byrow = T,nrow = 9)
mat3=mat2%*%mat1
mat3
#老師方法for回圈
mat5=matrix(data=rep(1,9^2),nrow=9)
for (i in 1:9) {
  for (j in 1:9) {
    #三種呈現方法
    #mat5[i,j]=i*j
    #mat5[i,j]=paste(i,"*",j,"=",i*j) #用paste黏貼
    mat5[i,j]=sprintf("%s*%s=%s",i,j,i*j)#用函數sprintf做字串正規化
  }
  
}
mat5
######function 
#py DEF fun 或 lambda
addThree=function(a){return(a+3)}#用函數function來自訂義函數,預設不寫return會回傳最後一行
addThree
addThree(3)  
#with default arguments
addThree_2=function(a=3){return(a+3)}
addThree_2() #不會ERROR
#每行程是結尾可加; 可不加
addThree=function(a){
            a+3;
}
#lazy function  
f2=function(a,b=2,c=NULL){   #參數給了3個 只用1個也不會報錯
  return(b+1)
}
f2
###對戰矩陣轉換
  r=read.csv("E:/BIG\ DATA下載/R/riii/data/match.txt",sep="|")
str(r)
class(r)
summary(r)
r[1,]
ma=matrix()

####迴圈涵式 
#py 的MAP fun  li=[1,2,3] list(map(lambda x:x+3,arr)#裡面是一個genterter)
#lapply sapply 對list或factor
x=list(c(1,2,3,4),c(5,6,7,8))
length(x)
lapply(x,sum) #lapply 回傳物件list   lapply裡面涵式名稱後面不用()
class(lapply(x,sum))
unlist(lapply(x,sum))
sapply(x,sum) #sapply 回傳物件vector 是lapply簡化的結果
class(sapply(x,sum))
lapply(x,addThree) #一個list 兩個vector
sapply(x,addThree)
class(sapply(x,addThree))#sapply回傳一個matrix  自動combin 兩個vector
##匿名涵式
lapply(x,function(e){e+3})
m1=matrix(1:4,byrow=T,nrow=2)
m2=matrix(5:8,byrow=T,nrow=2)
li=list(m1,m2)
lapply(li,function(e){e[1,]})
lapply(li,mean)
#apply 對陣列
m=matrix(1:4,byrow = T,nrow=2)
apply(m,1,sum)#rowsums
apply(m,2,sum)#colsums
rowSums(m)
row_meas=apply(m,1,mean)
col_meas=apply(m,2,mean)
#tapply
t=c(1,2,1,1,1,2)
x=c(80,70,65,88,70,65)
tapply(x,t,mean)
data(iris)
iris
#對每種花 都做 平均數 中位數 跟標準差
tapply(iris$Sepal.Length,iris$Species,function(e){list(avg=mean(e),md=median(e),s_D=sd(e))})
#取iris的欄位名稱  放到後面函數 做 以花的種類做 各欄位平均
s = lapply(names(iris[1:4]),function(e){tapply(iris[,e],iris$Species,mean) })
names(s) = names(iris[1:4]) #給個欄位名稱
s
###從Rdata檔讀寫
load("./cdc.Rdata") #不用設變數接她 因為當初是做到一半整個出去 回來是一個變數
save(x=iris,file="iir.Rdata") #檔名不等於變數名
cdc
str(cdc)
cdc$exerany=as.factoor(cdc$exerany)#BOOL轉回類別
cdc$hlthplan=as.factor(cdc$hlthplan)
cdc$smoke100=as.factor(cdc$smoke100)
cdc
######表格類別型
###一維次數分配表()
table(cdc$gender) #從分析只從一個角度切入
#相對比例
paste(table(cdc$gender)/nrow(cdc)*100,"%")#除總表的列
paste(table(cdc$gender)/length(cdc$gender)*100,"%") #除總樣本數
##二維次數分配表()
table(cdc$gender,cdc$exerany)
class(table(cdc$gender,cdc$exerany))
##三維次數分配表()
table(cdc$gender,cdc$exerany,cdc$genhlth)#第三維用條件表現
#算出男女抽菸與不抽菸的比例
table(cdc$gender)
m=table(cdc$gender,cdc$exerany) #男女抽菸的人數表
apply(m,1,function(e){e/sum(e)}) 
#####表格連續型
summary(cdc$height) #MIN48 MAX93
#20000筆 用公式做大概取組數 K>=15.2
seq(from=45,to=95,length.out=16)
seq(from=45,to=95,by=5)#分組位置超難看
length(seq(from=45,to=95,by=5))#11個數
cdc$group=cut(cdc$height,seq(from=45,to=95,by=5),right=F)#用參數改成包含下界 不包上界
table(cdc$group)
