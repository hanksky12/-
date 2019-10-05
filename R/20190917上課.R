#vector
#基礎運算
x=c(2,1,5)
y=c(3,5,2)
x+y
x-y
x*y
x/y
#不同長度
x=c(2,3,4,5)
x+10
x+c(10)
x+c(2,1)
x+c(2,1,2,1)
length(x)
#向量增加
c(1,2,3,4)
c(c(1),c(2),c(3),c(4))

#指定名稱
hight=c(120,110,180)
names(hight)=c("sky","hank","GG") 
hight 
names(hight) #元素名稱的向量

#判斷向量內容
c(1,5)>c(0,7)
hight>115
hight==120  #比較要兩個==
hight>115|hight<160  #或 or
hight>115&hight<160  #和 and

#篩選
hight[1] #index從1開始  1也是vector
hight[c(1,3)] 
#hight[1,3]  2維的列行表示  用在1維ERROR
hight[c("hank","GG")] #用元素名稱
hight[hight>115&hight<160] #用條件
hight[c(TRUE,FALSE,FALSE)] #布林向量篩選

#BMI
w=c(73,87,43)
names(w)=c("Brian","Toby","Sherry")
h=c(180,169,173)
names(h)=c("Brian","Toby","Sherry")
BMI=w/(h/100)^2
BMI[BMI<18.5|BMI>=24]

#seq()    類似python range()
seq(from=1,to=20) #從多少到多少 
for(i in seq(from=1,to=20)){print(i)}
seq(from=2,to=20,by=2) #間隔為2
seq(from=1,to=20,length.out = 2) #長度設定為2的數列
seq(from=1,to=20,length.out = 5)   
1:20  #簡寫 form=1 to=20 by=1  常用  
20:1

#rep()
rep(x=c(1),times=5)
rep(x=c(1,2),times=5) #重複5次
rep(x=c(1,2),length=5)#長度為5
rep(x=c(1,2),each=5)  #每一個元素重複5次
rep(x=c(1,2),times=c(1,2)) #很少用

#paste()  
#"dsfdf"+"fsdf" ERROR
paste("dsfdf","fsdf")
length(paste("dsfdf","fsdf")) #長度為1 有串接
paste("dsfdf","fsdf",sep="") #sep設定中間的串接符號
paste("dsfdf","fsdf",sep="@")
#paste()向量
c("H","f")
1:2
paste(c("H","f"),1:2,sep="_")
length(paste(c("H","f"),1:2,sep="_"))
paste(c("H","f"),1:2,sep="_",collapse = "$$") #少用

#Matrix
matrix(1:9,nrow = 3,ncol=3)  #9個元素=nrow x ncol  
matrix(1:9,nrow = 3)  #只要寫兩個就好 
a=matrix(1:9,nrow = 3,byrow=T) #預設byrow=FALSE
class(a)
c(h,w) #去觀察形成的vector  決定byrow=F or T
mat=matrix(data=c(h,w),nrow=3,byrow=F) 
rownames(mat)=c("Brian","Toby","Sherry")
colnames(mat)=c("hight","weight")
mat
dim(mat)#抓維度
nrow(mat)#抓列數
ncol(mat)#抓行數
t(mat)#轉置
mat[1,]#抓第一列
mat[,1]#抓第一行
mat[1,2]#抓第一列第二行
mat[c(1,2),1]#抓1.2列的第一行
mat[1:2,1]#結果同上  可用來抓區段的資料 上面寫法粉累
mat["Brian",]
mat[mat[,1]>170,] # 條件是第一行(身高)>170 的 "人"所以條件放在逗號前面

#新增row
mat
mat2=rbind(mat,c(200,70)) #新增的matrix 看要指定回原矩陣 或 指定到新的
mat2
rownames(mat2)
rownames(mat2)[4]="Sam"  #取名稱向量第四個  寫法 NO GOOD
rownames(mat2)[nrow(mat2)] ="SAM" #因為rbind加在矩陣最後一列 = 矩陣總列數
#新增col
mat3=cbind(mat2,c(1,2,3,4))
mat3
colnames(mat3)[ncol(mat3)]="不知道"
mat3
#加總 row or col
colSums(mat3) 
rowSums(mat3)#這邊沒啥意思
#平均 row or col
colMeans(mat3)

#matrix 基本運算
m1=matrix(1:4,byrow=T,nrow=2)
m2=matrix(5:8,byrow=T,nrow=2)
m1
m2
m1+m2   #+ - *  / 對應位置 
m1-m2
m1*m2  
m1/m2
m1%*%m2 #矩陣乘積 m1Xm2   注意兩矩陣的列行數 能不能相乘
#p27練習
m1=c(85,73)
m2=c(72,64)
m3=c(59,66)
ma=matrix(c(m1,m2,m3),byrow=T,nrow=3)
ma
w=c(0.4,0.6)
wa=matrix(w,nrow=2)#R這邊很聰明其實不用做2*1的矩陣 
wa
final=ma%*%wa #可以ma直接%*%c(0.4,0.6)  會自動轉2*1
rownames(final)=c("kevin","marry","jerry")
colnames(final)=c("總成績")
final


#Factor
weather=c("sunny","rainy","cloudy","rainy","cloudy")
class(weather)
weath_cat=factor(weather)  #共幾類
weath_cat 
class(weath_cat)
tmp=c("low","high","mid","high","mid","high")
tmp_cat=factor(tmp,ordered = T,levels = c("low","mid","high"))#自訂義 順序關西 少用
tmp_cat
#快速換類別名稱
weather=c("s","r","c","r","c")
weath_cat=factor(weather)
weath_cat
levels(weath_cat)=c("cloudy","rainy","sunny")#先去看原始資料的level的向量 一一對應名稱寫上
weath_cat

#type priority   轉換順序character>complex>numic>BOOL
c("string",1+2i,5.5,TRUE) #後面的元素都變成 character
c(1+2i,5.5,TRUE) #後面的元素都變成complex
c(5.5,TRUE) #後面的元素都變成numic
