#IOT p97
###集成學習 Ensemble Learning
# Bagging (Bootstrap aggregating) 
# Boosting 
# Stacking (also called meta ensembling)

#################################Bagging
#RF

############################Boosting Algorithms
####1.Adaboost 
#CART 
library(rpart) 
library(C50) 
data(churn)  
data_train = churnTrain[,-3]  # 排除 "area_code"欄位 
churn.tree=rpart(churn~.,data=data_train)
y = churnTest$churn 
y_hat=predict(churn.tree, newdata=churnTest, type="class") 
table.test=table(y,y_hat)
#預測正確率= 矩陣對角對角總和/ 矩陣總和 
cat("Correct Classification Ratio(test)=", sum(diag(table.test))/sum(table.test)*100,"%\n")

####Adaboost 建模
install.packages("fastAdaboost") 
library(fastAdaboost) 
churn_adaboost <- adaboost(churn~., data_train, 10) # 10表示有10個弱分類器 
pred <- predict( churn_adaboost,newdata=churnTest) 
cat("Correct Classification Ratio(test)=", (1-pred$error)*100,"%\n")

###2.Gradient Boosting
#讀入CSV檔：babies.csv 
babyData=read.table(file.choose(),header=T,sep = ",",row.names=NULL)
#排除有遺漏值的資料列 
babyData=na.exclude(babyData)
#訓練樣本70%與測試樣本30% 
n=0.3*nrow(babyData) 
test.index=sample(1:nrow(babyData),n) 
Train=babyData [-test.index,] 
Test=babyData[test.index,]
# 使用分類回歸樹 CART建模 
library(rpart) 
baby.tree=rpart(bwt~. ,data=Train) 
#MAPE 
y=babyData$bwt[test.index] 
y_hat=predict(baby.tree,newdata=Test, type="vector") 
test.MAPE=mean(abs(y-y_hat)/y) 
cat("MAPE(test)=",test.MAPE*100,"%\n")

###############GBM建模,預測問題(參數：損失函數distribution選擇 "gaussian") 
#install.packages("gbm") 
library(gbm) 
set.seed(123)
# distribution：損失函數 ; n.trees：迭代次數; interaction.depth：決策樹深度 # shrinkage: 就是learning rate避免過度訓練 ; bag.fraction建模一開始隨機選取訓練數據進行後續模型訓練的抽樣比率
bwt_GBM =gbm(bwt~.,data=Train, distribution= "gaussian",n.trees =5000,interaction.depth =4, shrinkage = 0.001, bag.fraction = 0.5,cv.folds=5 )
summary(bwt_GBM) #檢視變數重要性 

best.iter <- gbm.perf(bwt_GBM,method='cv')

plot(bwt_GBM, i=“gestation”) #繪圖檢視X變數與Y變數的關係 
y_hat=predict(bwt_GBM ,newdata =Test,n.trees =5000) 
test.MAPE=mean(abs(y-y_hat)/y)
cat("MAPE(test)=",test.MAPE*100,"%\n")

#########使用GBM建模,分類問題(參數：損失函數distribution選擇"bernoulli") 
#載入C50 churn資料集 
data(churn)  
#CART 
library(rpart) 
library(C50) 
data(churn)  
data_train = churnTrain[,-3]  # 排除 "area_code"欄位 
churn.tree=rpart(churn~.,data=data_train)
y = churnTest$churn 
y_hat=predict(churn.tree, newdata=churnTest, type="class") 
table.test=table(y,y_hat)
#預測正確率= 矩陣對角對角總和/ 矩陣總和 
cat("Correct Classification Ratio(test)=", sum(diag(table.test))/sum(table.test)*100,"%\n")

####Adaboost 建模
#install.packages("fastAdaboost") 
library(fastAdaboost) 
churn_adaboost <- adaboost(churn~., data_train, 10) # 10表示有10個弱分類器 
pred <- predict( churn_adaboost,newdata=churnTest) 
cat("Correct Classification Ratio(test)=", (1-pred$error)*100,"%\n")

#GBM建模
set.seed(123) 
data_train$churn = ifelse(data_train$churn=='yes',1,0) #GBM的Y變數僅識別 0與1
# 交叉驗證組數# GBM作者建議shrinkage參數設在0.01 ~ 0.001之間 # n.trees參數設在3000-10000之間
churn_GBM =gbm(churn~., data=data_train , distribution= "bernoulli",n.trees =10000, interaction.depth =4,  shrinkage = 0.01,  bag.fraction = 0.5,  cv.folds=5  ) 
# 用交叉驗證確定最佳迭代次數
best.iter <- gbm.perf(churn_GBM,method='cv')
#利用最佳迭代次數再次建模
churn_GBM =gbm(churn~., data=data_train , distribution= "bernoulli",n.trees =best.iter, interaction.depth =4,  shrinkage = 0.01,  bag.fraction = 0.5,  cv.folds=5  ) 
summary(churn_GBM ) #檢視變數重要

#評分
data_test <- churnTest 
data_test$churn = ifelse(data_test$churn=='yes',1,0)  #將yes/no轉為 1/0
pred=predict(churn_GBM ,newdata = data_test,n.trees = best.iter)
#繪製 ROC圖 
#install.packages("stats")
#install.packages("pROC")
library(stats)
library(pROC) 
churn.roc = roc(data_test$churn,pred) 
plot(churn.roc)

#利用coords函數找出 切割1/0的最佳臨界值 threshold 
coords(churn.roc,"best")
churn.predict.class = ifelse(pred> coords(churn.roc,"best")["threshold"],"yes","no") 
table(data_test$churn,churn.predict.class)
table.test <- table(data_test$churn,churn.predict.class)

#預測正確率 = 矩陣對角對角總和 / 矩陣總和 
cat("Correct Classification Ratio(test)=", sum(diag(table.test))/sum(table.test)*100,"%\n")

####################################XGBoost建模 
#客戶流失模(二元分類)
install.packages("xgboost")
library(xgboost) 
library(C50)
library(dplyr)

#以客戶流失資料集為例 
data(churn)   
data_train = churnTrain[,-3] #data.frame:   3333 obs. of  19 variables 
data_test = churnTest[,-3]

#將訓練與測試資料集轉乘數值型的Matrix格式 
dataTrain_matrix <- Matrix::sparse.model.matrix(churn ~ .-1, data = data_train) #-1 是去掉流水號
output_vector_train = churnTrain[,'churn'] == "yes" 
train_matrix <- xgb.DMatrix(data = as.matrix(dataTrain_matrix),label=output_vector_train)
dataTest_matrix <- Matrix::sparse.model.matrix(churn ~ .-1, data = data_test) > output_vector_test = churnTest[,'churn'] == "yes" > test_matrix <- xgb.DMatrix(data = as.matrix(dataTest_matrix),label=output_vector_test)

# 模型超參數設定
nc = length(unique(output_vector_train)) #預測變數Y有幾類 
#結果包含預測機率與預測類別 #損失函數# 設定Y的類別 
params = list( "objective" = "multi:softprob",  "eval_metric" = "mlogloss", "num_class" = nc ) 
watchlist <- list(train=train_matrix , test=test_matrix) #設定建模時需監控的樣本清單

# xgboost模型建置 
# Learning Rate, low -> more robust to overfitting #預設值:6，每顆樹的最大深度，樹高越深，越容易overfitting 
bst_model <- xgb.train(params = params, data = train_matrix, nrounds = 100, watchlist = watchlist, eta = 0.3,  max.depth = 5, seed =123 )

# Overfitting檢視 
evalue_log <- bst_model$evaluation_log 
plot(evalue_log$iter, evalue_log$train_mlogloss, col='blue') 
lines(evalue_log$iter, evalue_log$test_mlogloss, col='red')
# 依照最佳迭代次數再次建模 
bst_model <- xgb.train(params = params, data = train_matrix, nrounds = 17, watchlist = watchlist, eta = 0.3,  max.depth = 5, seed =123 )
#檢視重要變數 
var_feature <- xgb.importance(colnames(train_matrix), model = bst_model) 
print(var_feature) > xgb.plot.importance(var_feature)

#預測新資料 
p <- predict(bst_model, newdata = test_matrix) #模型評分，1667*2筆(因為每人有流失與未流失的機率) 
pred <- matrix(p, nrow=nc, ncol=length(p)/nc ) %>% #轉成 2*1667 matrix格式
  t() %>%   #再轉成 1667*2 matrix格式 
  data.frame() %>%   #轉成data.frame格式 
  mutate(label = output_vector_test, max_prob = max.col(., "last")-1 )#取得最大機率值的欄位數，然後將欄位編號減1

#預測正確率 = 矩陣對角對角總和 / 矩陣總和 
table.test = table(output_vector_test,pred$max_prob) 
cat("Correct Classification Ratio(test)=", sum(diag(table.test))/sum(table.test)*100,"%\n")

#p121 建置臭氧濃度預測模型
# 資料集介紹 
?airquality

#Step1. 連結MongoDB Step2. 整理 Allitems Step3. 建模 Step4. 預測臭氧濃度

# Mongodb 
install.packages('mongolite')
library(mongolite)

#Step1.連接MongoDB 
host <- "192.168.56.1" 
port <- "27017" 
database <- "test123" 
URL <- paste0("mongodb://",host,":",port,"/",database) #paste0 會去除空格

##iris練習
#上傳iris
con <- mongo(collection="iris test", db = "test123", url = URL)#新增一個空白文件
con$insert(iris)#上傳iris
#下載iris test文件
documents <- con$find()
str(documents)


#上傳sensor  airquality   練習上傳mongodb
sensor=read.csv("./sensor.csv",header=T,sep="",fileEncoding = "big5")
airquality=read.csv("./airquality.csv",header=T,sep="",fileEncoding = "big5")

con <- mongo(collection="sensor", db = "test123", url = URL)
con$insert(sensor)

con <- mongo(collection="airquality", db = "test123", url = URL)
con$insert(airquality)

#清理變數
rm(sensor)

#從mongoDB抓資料
#東西原本是data.frame塞到mongodb 上面都是json格式,回來又變成data.frame
con <- mongo(collection="sensor", db = "test123", url = URL)
sensor <- con$find()
str(sensor)
con <- mongo(collection="airquality", db = "test123", url = URL)
airquality <- con$find()
str(str(sensor))

# Step 2 整理機器學習演算法所需的資料 allitems
# 安裝sqldf,利用SQL語法整理資料 
#install.packages("sqldf") 
library(sqldf)

# 將sensor收集的資料整理成 月, 日, 當日平均溫度, 當日平均濕度,然後透過月、日與 airquality 作資料勾稽(Left join)
df_sensor <- sqldf("SELECT cast(substr(trim(dt),7,1) as int) month ,cast(substr(trim(dt),9,2) as int) day ,avg(temperature) avg_temperature ,avg(humidity) avg_humidity FROM sensor group by cast(substr(trim(dt),7,1) as int) ,cast(substr(trim(dt),9,2) as int) having cast(substr(trim(dt),7,1) as int) <>0 ")
#join
df_allitems <- sqldf(" select a.*,b.avg_temperature,b.avg_humidity from airquality a left join df_sensor b on a.Month=b.month and a.Day = b.day ")

# Step 3 建置多元回歸模型
lmTrain <- lm(formula = Ozone ~ Solar_R+Wind+avg_temperature+avg_humidity, data = subset(df_allitems, complete.cases(df_allitems))) #排除null

# 模型摘要
summary(lmTrain ) 

# Step 4 預測明日臭氧濃度 
New_data <- data.frame(Solar_R=200, Wind=12, avg_temperature=32.1, avg_humidity =62.7)
predicted <- predict(lmTrain , newdata = New_data) 
predicted/1000 
# 結束連線 
rm(con)
gc()
