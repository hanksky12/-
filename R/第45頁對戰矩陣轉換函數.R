#P45對戰矩陣轉換
input_info=read.table("./match.txt",header = F,sep="|")
str(input_info)
tr_fun=function(e) {
  #隨便挑一行  把人名整理  人數整理 
  atoz=levels(factor(e[,1]))
  row_n=length(atoz)
  #做出  對應大小空矩陣 
  mat=matrix(rep(1,row_n^2),nrow=row_n)
  #給列,行名稱向量
  rownames(mat)=atoz
  colnames(mat)=atoz
  for (i in 1:row_n) {
    for (j in 1:row_n){
      #對每個元素做條件判斷
      if (atoz[i]!=atoz[j]){
        #把人名回去對應原DATA的第一行跟第二行,得到兩個BOOL vactor取交集後
        #再把最後的BOOL vactor去原DATA找值
        mat[i,j] = e[atoz[i]==e[,1]&atoz[j]==e[,2],3]
      }else{
        mat[i,j]=-1}
    }
    
  }
  mat
}
####老師的
tr_fun(input_info)
#有無header   分隔符號都可由使用者決定 
match_func2 = function(filename,header=F,sep='|'){
  match_df = read.table(filename,header = header,sep=sep)
  #1.一開始填-1省事#2. dimnames由長度是2的list裡面放rownames,colnames
  mat = matrix(data=-1,nrow=length(levels(match_df[,1])),ncol=length(levels(match_df[,2])),dimnames = list(levels(match_df[,1]),levels(match_df[,2])))
  for(i in 1:nrow(match_df)){
    mat[match_df[i,1],match_df[i,2]] = match_df[i,3]
  }
  mat
}