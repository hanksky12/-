#P55
#統計值
a = c(173,178,173,168,160,173,168,173,185,175,178,182)#身高
mean(a)#=====>平均數
sort(a)
median(a)#========>中位數 奇數中間的那個數 偶數中間兩個做平均
table(a) #用統計方式看資料的累積次數
max(table(a)) #最多的資料有幾個
which.max(table(a)) #該數在table的位置
names(which.max(table(a))) #該數的名稱  ======>眾數(沒有可用的涵數)

#離差量數:range IQR variance stardard deviation
load("./cdc.Rdata")
#全距
range(cdc$height)
#四分位距
IQR(cdc$height)
#變異數
var(cdc$height)
#標準差
sqrt(var(cdc$height))
sd(cdc$height)
#摘要數據
summary(cdc$height)
### Covariance & Correlation
cdc[,c('height','weight','wtdesire','age')]#先取出想要做相關的欄位
cov(cdc[,c('height','weight','wtdesire','age')])
cor(cdc[,c('height','weight','wtdesire','age')])#相關係數矩陣
#######################繪圖套件
#內建套件graphics
#類別資料都要table
table(cdc$height)

#屬貭資料
par(mfrow=c(1,3))#畫布 1*3的圖 可塞多張圖在同張圖
#長條圖
barplot(table(cdc$smoke100))
?barplot
barplot(table(cdc$smoke100),xlab='有無吸菸',ylab='人數',main='有無吸菸習慣',col='blue',family="Songti SC")

#圓餅圖
pie(table(cdc$smoke100))
pie(table(cdc$genhlth))
pie(table(cdc$genhlth),col = rainbow(5))

rainbow(5)
#加上各分類比例
pct = round(table(cdc$genhlth) / length(cdc$genhlth) *100,1)#round四捨五入  ,1==>小數點後1位做四捨五入
labels = paste(names(pct),pct,"%")  #轉文字黏起來
pie(table(cdc$genhlth), labels = labels)

#馬賽克圖
gender_smokers = table(cdc$gender,cdc$smoke100)
mosaicplot(gender_smokers)

#連續型資料
#直方圖

hist(cdc$height)#breaks 切割 裡面有公式
hist(cdc$height,breaks=30)
hist(cdc$height,breaks=50)

#莖葉圖
stem(cdc$weight)
tmp=sample(cdc$age,100)#樣本抽樣涵數
stem(tmp)

#盒鬚圖 (箱型圖)
boxplot(cdc$weight)
boxplot(cdc$weight,horizontal = T)
#~右邊帶入要分組的資訊 ~左邊帶入要分組的資料
boxplot(cdc$weight~cdc$gender) 
bmi=(cdc$weight/cdc$height^2)*703
boxplot(bmi~cdc$genhlth)

#觀察兩組資料間的關係:點散布圖
par(mfrow=c(1,3))
plot(cdc$weight,cdc$height)
plot(cdc$weight,cdc$wtdesire)
plot(cdc[,c("height","weight","wtdesire")])#依樣可以丟DATA FRAME

#圖片輸出
png(filename="test789.png")
plot(cdc[,c("height","weight","wtdesire")])
dev.off()
#手動右邊 Plots 有 Export 做輸出

##Data   Explorer 將資料輸出成文件資訊
#用法 使用在剛拿到一筆data 做一些初步觀察 
install.packages("DataExplorer")
library(DataExplorer)
help(package = 'DataExplorer')
data(iris)
dummify(iris)#將類別型資料轉成dummify資料衍生出欄位 用1,0顯示
head(dummify(iris))

create_report(iris)
introduce(iris)
dummify(iris)
plot_missing(iris) #遺失值
plot_histogram(iris) #直方圖
plot_boxplot(iris,by='Species') #盒鬚
plot_correlation(iris[-5]) #相關係數
plot_prcomp(iris)

##ggplot2套件 ==>主流
#不用分連續或類別  沒有圓餅圖可用
##### documentation
http://docs.ggplot2.org/current/
  
##### cheat sheet
https://www.rstudio.com/wp-content/uploads/2015/03/ggplot2-cheatsheet.pdf
library(ggplot2)
load("./cdc.Rdata")
g=ggplot(cdc,aes(x=height,y=weight))#整個資料拉進來
g#空白底層
g+geom_point()
g+geom_boxplot()
k=ggplot(cdc,aes(x=height))
k+geom_density()
u=ggplot(cdc,aes(x=height,y=weight,col=gender))#用顏色來表示性別
u+geom_point()
e=ggplot(cdc,aes(x=height,y=weight))#形狀來表示性別
e+geom_point(aes(shape=gender))
g+ylab("count")+ggtitle("HHH")
#fill=>填滿顏色 color=>邊線顏色
g <- ggplot(cdc,aes(x=genhlth))
g+geom_bar()#長方圖
g+geom_bar() + ylab('次數') 
g+geom_bar(fill='snow',color='black')
g+geom_bar(aes(fill=gender),color='black')######跟資料有關放進aes
g+geom_bar(aes(fill=gender))+ylab("次數")+ggtitle("健康狀況長條圖")

#theme 主題
g+geom_bar()+theme_dark()
g+geom_bar(aes(col=gender))+ylab("次數")+ggtitle("健康狀況長條圖") + theme(text=element_text(size=16,  family="Songti SC"))#stat funtion
#每種幾何圖形都是對應到一種運算
?geom_bar
g+geom_bar()#裡面有count函數
g+stat_count()
##position
g+stat_count(aes(fill=gender))
g=ggplot(cdc,aes(x=gender))
g
g+geom_bar(aes(fill=genhlth),position = "stack")
g+geom_bar(aes(fill=genhlth),position = "dodge")#並排  清楚看出同bar裡面比例高低
g+geom_bar(aes(fill=genhlth),position = "fill")#兩條等長  不同性別某類別的比例
g+geom_bar(aes(fill=genhlth),position = "identity")

#Facets法
g=ggplot(cdc,aes(x=weight))
g+geom_histogram()+facet_wrap(~genhlth)#~左邊資料已經進去了
g+geom_histogram()+facet_wrap(~gender)#
g+geom_histogram()+facet_grid(~gender)
g+geom_histogram()+facet_wrap(genhlth~gender)

#coordinate
g=ggplot(cdc,aes(x=genhlth))
g+geom_bar()+coord_flip()
g+geom_bar()+coord_polar(theta = "x")#極座標 (當圓餅圖)5種類別 1種72度  南丁格爾玫瑰圖 次數越多花瓣越大
g+geom_bar()+coord_polar(theta = "y")#玉環圖  次數越多該條越長
g+geom_bar(aes(fill=gender))+coord_polar(theta = "y")

#pie chart
#用一個長方圖轉極座標圖
ggplot(cdc,aes(x=1)) + geom_bar(aes(fill=genhlth)) + coord_polar(theta = 'y')


####幫dataframe 做名稱向量
#舊寫法
precounted = as.data.frame(table(cdc$genhlth))
names(precounted)[1]= 'genhlth'
precounted
#新寫法
#幫元素名稱向量 取名稱 dnn
df=as.data.frame(table(cdc$genhlth,dnn=c("GENHLTH")))
str(df)
names(df)
df
#####繪製預先分組的資料
ggplot(df,aes(x=GENHLTH))
ggplot(df,aes(x=GENHLTH))+geom_bar()
k=ggplot(df,aes(x=GENHLTH,y=Freq))+geom_bar(stat = "identity")


#save
ggsave(filename = "GENHLTH.png",plot=k)#plot 畫完圖丟進去的變數名稱
## antv documentation  甚麼時候該用甚麼樣的圖
https://antv.alipay.com/zh-cn/vis/chart/index.html

## Esquisse  GUI界面
install.packages('esquisse')
install.packages("httpuv")
library('esquisse')
esquisse::esquisser()
#選擇資料集
#選擇欄位
#型態轉換(如果覺得預設有錯)
#左上選圖 中間拉軸
#用法跟ggplot語法相同
#可直接出圖 或 呈現程式碼

#
load("./appledaily.RData")
getwd()
str(appledaily)
as.POSIXct(appledaily[1,'dt'],format='%Y年%m月%d日%H:%M')

#######比較as.POSIXct() 和 as.POSIXlt()
####posixct()    unclass 解開是Epoch time
####posixlt() unclass 解開是 區分開年月日時分秒
#Epoch time: UTC1970年1月1日0時0分0秒起至現在的總秒數  不用擔心時區轉換日期問題   在DB裡面老師都是用Epoch time存時間
#posixlt() unclass 月份會少1  年會少1900

t1 = as.POSIXct(appledaily$dt,format = '%Y年%m月%d日%H:%M')
class(t1)
head(unclass(t1))

t2 = as.POSIXlt(appledaily$dt,format = '%Y年%m月%d日%H:%M')
class(t2)
unclass(t2)

appledaily$dt = as.POSIXct(appledaily$dt,format = '%Y年%m月%d日%H:%M')
str(appledaily)
#時間套件lubridate
install.packages("lubridate")

#https://r4ds.had.co.nz/dates-and-times.html
## Extracting information
now_date=now()#抓系統時間

year(now_date)
month(now_date,label=T)
day(now_date)
hour(now_date)
minute(now_date)
second(now_date)
wday(now_date,label=T)

### Parsing dates and times
ymd(20190912)#年月日
mdy(02032018)#月日年
dmy(02032018)
ymd("2019.09.12") #各種格式都能讀
ymd("2019@09@12")
ymd('2019/01/29')
ymd_hm()
ymd_hm('2019/1/29 14:40',tz='Asia/Taipei')
with_tz(ymd_hm('2019/1/29 14:40',tz='Asia/Taipei'),tzone='America/Los_Angeles') #轉換時區
appledaily$dt = ymd_hm(appledaily$dt)

#方法一:利用sub函數取代  (py replace())
appledaily$clicked[1]
tmp=sub("人氣\\(","",appledaily$clicked[1])#前面放要換的 中間換完的 後面原資料
tmp2=sub("\\)","",tmp)
c=as.numeric(tmp2)

clicked = sub('\\)','',sub('人氣\\(','',appledaily$clicked))
clicked = as.integer(clicked)
head(clicked)

#方法二:正規表達法:使用stringr套件的str_match()   (py match())
library(stringr)
#正規表達法
# "." => 0~多個
# "+" =>1~多個
# "?" =>0 or 1
#\d 抓數字 \s 抓文字

str_match(appledaily$clicked,"人氣\\((\\d+)\\)")[,2]
clicked = as.integer(str_match(appledaily$clicked,"人氣\\((\\d+)\\)")[,2])

appledaily$clicked = clicked
head(clicked)

 ### 其他常見字串處理函式
#gsub 全部取代  sub 只會取代從左邊遇到的第一個
#利用gsub函數取代
s = "aaa bbb ccc aaa bbb aaa"
sub("aaa","",s)
gsub("aaa","",s)
#grep()====>回傳目標字串的 index          
test_str = c('abcd','bcd','cde')
grep('a',test_str)
test_str[grep('a',test_str)]
grep("中國",appledaily$title)
appledaily[grep("中國",appledaily$title)[1:5],]


#strsplit()===>字串分割 從符號去抓
s=strsplit()
#unlist  裡面是多元素的向量


#substring===>取出部分字串 從index 去抓
test_s="asddsd"

#grep()  ==> return index


          
#grepl() ==> return boolean 
grepl('a',test_str)
test_str[grepl('a',test_str)]
          
#strsplit() ==> 字串分割
splited = strsplit(c('abc-def','ddd-ggg'),'-')
splited
class(splited)
### 取出list裡面部分元素
sapply(splited,function(e){e[1]})
unlist(splited)[seq(from=1,to=4,by=2)]
#substring() ==> 取得部份字串
test_s = 'abcdef'
nchar(test_s)
substring(test_s,2,nchar('abcdef')-1)