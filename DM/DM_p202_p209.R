#PCA主成分分析 (自動萃取主成分)   P202
library(C50) 
data(churn) 
data <- churnTrain[,c(-1,-3,-4,-5,-20)] # 不要第1, 3, 4, 5, 20欄 
pca_Traindt<- princomp( data , cor=T) # cor=T 單位不同 
summary(pca_Traindt)  ###查看累積資訊量 挑幾個看人
screeplot(pca_Traindt,type="lines") #繪製陡坡圖 (參考用 實際上要看帶進去的效果)
print(pca_Traindt$loadings, digits = 8, cutoff=0)  #cutoff=0表示接近0也要顯示 (通常不會看)

p <- predict(pca_Traindt) #直接算出主成分 對應
head(p,5)
p[,c(1:7)] #取出7個主成分


############KNN演算法 P215
install.packages("class")
library(class)
data(iris)
#(1)設定亂數種子 
set.seed(123)
#(2)取得資料筆數 
n <- nrow(iris)
#(3)取得訓練樣本數的index，70%建模，30%驗證 
train_idx <- sample(seq_len(n), size = round(0.7 * n))
#(4)產出訓練資料與測試資料 
traindata <- iris[train_idx,]
testdata <- iris[ - train_idx,]
train_y <- traindata[,5] 
test_y <- testdata[,5]
#(5)設定K，K通常可以設定為資料筆數的平方根，記得檢查k的奇偶 +1或-1
k_set <- as.integer(sqrt(n)) #12
k_set=k_set+1
#(6)建立模型 
pred <- knn(train = traindata[-5], test = testdata[-5], cl = train_y, k = k_set)
#(7) 混淆矩陣計算準確度 
message("準確度：",sum(diag(table(pred,test_y))) / sum(table(pred,test_y)) *100,"%")  ### ACC計算 對角線/全部


######################決策樹
# 一次安裝所有packages 
packages <- c("C50","tree", "rpart","randomForest") 
for (i in packages){  install.packages(i) } 
#一次載入packages 
sapply(packages, FUN = library, character.only = TRUE)
search()#目前library套件

#######C5.0
#訓練樣本70%, 測試樣本30% 
install.packages("caret") #幫忙切樣本的套件 而且分佈漂亮，不用人工測試
library(caret) 
sample_Index <- createDataPartition(y=iris$Species,p=0.7,list=FALSE) 
iris.train=iris[sample_Index,] #訓練樣本
iris.test=iris[-sample_Index,] #測試樣本
#確認訓練樣本與測試樣本分不一致 
par(mfrow=c(1,1)) #讓R的繪圖視窗切割成 1 X 2 的方塊 
plot(iris.train$Species) 
plot(iris.test$Species)
#C5.0模型訓練 
iris.C50tree=C5.0(Species~.,data=iris.train) 
summary(iris.C50tree) 
plot(iris.C50tree)

#訓練樣本的混淆矩陣(confusion matrix)與預測正確率 
y = iris$Species[sample_Index] 
y_hat= predict(iris.C50tree,iris.train,type='class') 
table.train=table(y,y_hat) #做混淆矩陣
cat("Total records(train)=",nrow(iris.train),"\n") 
#預測正確率 = 矩陣對角對角總和 / 矩陣總和 
cat("Correct Classification Ratio(train)=", sum(diag(table.train))/sum(table.train)*100,"%\n")
#測試樣本的混淆矩陣(confusion matrix)與預測正確率 
y = iris$Species[-sample_Index] 
y_hat= predict(iris.C50tree,iris.test,type='class')
table.test=table(y,y_hat) #做混淆矩陣
cat("Total records(test)=",nrow(iris.test),"\n") 
cat("Correct Classification Ratio(test)=", sum(diag(table.test))/sum(table.test)*100,"%\n")

##########隨機森林
#模型訓練 
iris.RFtree = randomForest(Species ~ ., data=iris.train, importane=T, proximity =TRUE, ntree=400)
print(iris.RFtree )
#變數重要性 
round(importance(iris.RFtree),2)
#訓練樣本的混淆矩陣(confusion matrix)與預測正確率
table.rf=iris.RFtree$confusion 
cat("CORRECTION RATIO(train)=", sum(diag(table.rf)/sum(table.rf))*100,"%\n")
#測試樣本的混淆矩陣(confusion matrix)與預測正確率 
y = iris$Species[-sample_Index] 
y_hat= predict(iris.RFtree ,newdata=iris.test) #給預測的結果
y_hat= predict(iris.RFtree ,newdata=iris.test,type="prob") #給結果的預測機率值 ，前面建模要開proximity =TRUE
table.test=table(y,y_hat) 
cat("Correct Classification Ratio(test)=", sum(diag(table.test))/sum(table.test)*100,"%\n")


###########分類迴歸樹
data(churn)
#模型訓練 
data_train= churnTrain[,-3-8-9-11-12-14-15-17-18] # 排除 "area_code"欄位 
data_train= churnTrain[,-3]
churn.tree=rpart(churn~.,data=data_train) 
churn.tree
# 繪製CART決策樹
plot(churn.tree) 
text(churn.tree,cex= .8) #cex表示字體大小
# 變數重要性 
churn.tree$variable.importance
#訓練樣本的混淆矩陣(confusion matrix)與預測正確率 
y = churnTrain$churn 
y_hat=predict(churn.tree,newdata=churnTrain,type="class") 
table.train=table(y,y_hat) #預測正確率= 矩陣對角對角總和/ 矩陣總和 
cat("Correct Classification Ratio(train)=", sum(diag(table.train))/sum(table.train)*100,"%\n")
#測試樣本的混淆矩陣(confusion matrix)與預測正確率 
y = churnTest$churn 
y_hat=predict(churn.tree,newdata=churnTest,type="class") 
table.test=table(y,y_hat) #預測正確率= 矩陣對角對角總和/ 矩陣總和
cat("Correct Classification Ratio(test)=", sum(diag(table.test))/sum(table.test)*100,"%\n")

######gain lift 作業

#########ROC曲線 AUC係數 GINI係數
# 測試樣本評分 
y_prob= predict(churn.tree,newdata=churnTest,type="prob")[,1] #取正例預測機率
# ROC Curve 
install.packages("ROCR") 
library(ROCR) 
pred<- prediction(y_prob, labels = churnTest$churn)
# tpr: True Positive Ratio 正確預測正例; # fpr: False Positive Ration誤判為正例 
perf <- performance(pred, "tpr", "fpr") 
plot(perf) > points(c(0,1),c(0,1),type="l",lty=2)  #畫虛線
#AUC 
perf <- performance(pred, "auc") 
(AUC = perf@y.values[[1]])
( Gini = (AUC-0.5) *2 )*100
# Lift chart
perf <- performance(pred, "lift" , "rpp") 
plot(perf)


########羅吉斯迴歸
#載入C50 churn資料集
data(churn)   #載入C50 churn資料集 
data_train= churnTrain[,-3] # 排除 "area_code"欄位 
data_train= churnTrain[,-1] # 排除 “state"欄位 
data_train$churn= ifelse(data_train$churn=='yes',1,0)  # 羅吉斯回歸預設對y=1 建模產出推估機率
#模型訓練
logitM=glm(formula=churn~., data= data_train, family=binomial(link="logit"), na.action=na.exclude)#binomial 二項分佈 排除空值na.action
summary(logitM)
#訓練樣本的混淆矩陣(confusion matrix)與預測正確率 
install.packages("InformationValue")# for optimalCutoff 
library(InformationValue) 
y = data_train$churn # 0或1
y_hat=predict(logitM,newdata=churnTrain,type="response") #0~1的機率值
#optimalCutoff(y, y_hat)[1] 提供了找到最佳截止值，減少錯誤分類錯誤
optimalCutoff(y, y_hat)
optimalCutoff(y, y_hat)[1]
table.train=table(y, y_hat>optimalCutoff(y, y_hat)[1]) #後面BOOL向量
#預測正確率= 矩陣對角對角總和/ 矩陣總和 
cat("Correct Classification Ratio(train)=", sum(diag(table.train))/sum(table.train)*100,"%\n")


################## SVM 支持向量機
install.packages("e1071") 
library(e1071) 
data(iris) 
data <- iris
# 產生建模與測試樣本 
n=0.3*nrow(data) 
test.index=sample(1:nrow(data),n) 
Train=data[-test.index,] 
Test=data[test.index,]
# 建模 
svm = svm(Species ~ . ,data=Train) 
summary(svm)
# 測試樣本預測正確率 
Ypred= predict(svm, Test)
#  混淆矩陣(預測率有93.33%) 
message("準確度：",sum(diag(table(Test$Species,Ypred))) / sum(table(Test$Species,Ypred)) *100,"%")


####分群方法
############## K-means
iris_new <- iris[, -5] 
set.seed(123)
Cluster_km <- kmeans(iris_new, nstart=15,centers=3) # center就是設定群數 # nstart 是指重新隨意放 k 個中心點的次數, 一般建議 nstart >= 10 
table(Cluster_km$cluster, iris[, 5]) #觀察分群結果與實際類別的差別
plot(iris_new $Petal.Width, iris_new $Petal.Length, col=Cluster_km$cluster)
