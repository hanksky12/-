#DM P106
data(cars)
str(cars)
#######數據分箱
# 將速度分成3類 第一類 speed<12 第二類 speed <15 第三類 speed >= 15
cars$speed
x=cars$speed
x<12
new_cars_band=1*(x<12)+2*(x>=12 & x<15)+3*(x>=15)###聰明的轉法 要學
#  4==> 1*(TRUE)+2*(FALSE)+3*(FALSE)===>1*1+2*0+3*0=1
#  25===>1*(FALSE)+2*(FALSE)+3*(TRUE)====>1*0+2*0+3*1=3
new_cars_band
label=c("慢","中","快")
new_cars_band=label[new_cars_band]  #用index 對應要寫對
new_cars_band
#用ifelse 巢狀粉快
ifelse(x<12,"慢",ifelse(x>=15,"快","中"))
x

####慢中==>一般轎車 快==>跑車
car_categ=c("一般轎車","跑車")
new_cars_band_1=1*(new_cars_band %in% c("慢","中"))+2*(new_cars_band %in% c("快"))
new_cars_band_1=car_categ[new_cars_band_1]
new_cars_band_1
#用ifelse 粉快
new_cars_band_3=ifelse(new_cars_band&in&c("慢","中"),"一般轎車","跑車")

####將一般轎車轉1 跑車轉0
new_cars_band_2=1*(new_cars_band_1%in%c("一般轎車"))+0*(new_cars_band_1%in%c("跑車"))
#用if else
new_cars_band_2=ifelse(new_cars_band_1=="一般轎車",1,0)


#P108
#with in
new_cars=cars
new_cars=within(new_cars,{
  speed_level=NA#不寫不行
  speed_level[cars$speed<12]="慢"
  speed_level[cars$speed>=12 & cars$speed<15]="中"
  speed_level[cars$speed>=15]="快"
  
})
new_cars

#p109
#transform
new_cars <- cars 
new_cars <- transform(new_cars, 
                      new_var1 = new_cars$speed * new_cars$dist , 
                      new_var2 = new_cars$dist * 100
)
head(new_cars,10) 

#P114
##########兩表join
a <- data.frame(T_name=c('Tony','Orozco','Justin'), Age=c(25,24,26)) 
a 
b <- data.frame(T_name=c('Tony','Orozco','Justin','Carol'), Salary=c(20000,25000,30000,18000)) 
b
###inner join
merge(a,b,by.x="T_name",by.y = "T_name")
###left join
merge(b,a,by.x="T_name",by.y = "T_name",all.x = T)

#P117
#SQL套件 (標準sql語法)
install.packages("sqldf")
library(sqldf)
sqldf("select * from iris")
sqldf("select Species,count(*) cnt from iris group by Species")
class(sqldf("select Species,count(*) cnt from iris group by Species"))##回傳data frame

#p119
################################切割(不同類型資料混在一起對建模出來的成效不好)
#split 函數
data("chickwts")
table(chickwts$feed)
spl=split(chickwts$weight,chickwts$feed)
spl
##指標
#sample 函數 隨機抽樣
chickwts[sample(1:nrow(chickwts),5,replace = F),] #sample 函數 全部列 抽5筆 取後不放回
##邏輯方法=======<常用
High <- c( 120, 134, 110, 158, 100, 101, 140, 105) 
Weight <- sample(20:25,8,replace = TRUE) #seq 20-25
Gender <- c("男", "女", "男", "男", "男", "女", "女", "女")
High>130
High[High>130]
Gender[High>130]
report=data.frame(High,Weight,Gender)
boy=report[Gender=="男" & High>130,]
boy

#p142 要去考中華電信 這個要熟
install.packages("C50")
library(C50)
?(churn)
data(churn)
str(churnTrain)#訓練樣本

#p148
##相關係數
High <- c( 120, 134, 110, 158, 100, 101, 140, 105) 
Weight <- sample(20:28,8) 
cor(High,Weight)

#p149
data("airquality")
head(airquality,6)
####cor矩陣
cor(airquality[,1:4],use = "pairwise")
####cor繪圖
pairs(airquality[,1:4])
