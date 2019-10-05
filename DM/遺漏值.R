tmp=c(2,3,8,NA,4,NA,9,12,NA)#na要大寫
is.na(tmp) 
any(is.na(tmp))#針對是否有missing data回傳true或false值
sum(is.na(tmp))#計算全部的missing數值數量 
is.nan(0/0)
is.infinite(1/0)
summary(tmp) #summary也可看出遺漏值數量
