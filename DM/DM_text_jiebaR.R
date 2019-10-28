##########Jieba 介紹
install.packages("jiebaR")
library(jiebaR)
#建立分詞器
seq_worker=worker()
#分詞
segment("我是一段文本",seq_worker)

#####爬蟲
install.packages("devtools") 
install.packages("tidyRSS") 
install.packages("XML") 
install.packages("RCurl") 
install.packages("plyr") 
install.packages("wordcloud") 
install.packages("wordcloud2")

library(tidyRSS) 
library(XML) 
library(RCurl)
library(jiebaR) 
library(stringr)
library(plyr) 
library(wordcloud) 
library(wordcloud2)
library(tidyRSS) 

#############針對RSS
rss_url <- 'https://udn.com/rssfeed/news/1013/7113/7471?ch=news' 
rss <- tidyRSS::tidyfeed(feed = rss_url) #### 因為tidyfeed 是靜態方法  在R裡面要用::去呼叫 tidyRSS是實例
rss$feed_title # RSS標題 
rss$feed_link # RSS超連結 
rss$feed_description # 說明 
rss$feed_language # 語系 
rss$item_title # 文章標題 
rss$item_link # 文章超連結
#爬蟲事前偽裝準備  
ua <- "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36"
myHttpHeader <- c(
  "User-Agent"=ua,
  "accept"="text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3",
  "accept-encoding"= "gzip, deflate, br",
  "accept-language"="zh-TW,zh;q=0.9,en-US;q=0.8,en;q=0.7",
  "cache-control"="max-age=0",
  "referer"="https://udn.com/news/index",
  "sec-fetch-mode"= "navigate",
  "sec-fetch-site"="same-site",
  "sec-fetch-user"= "?1",
  "upgrade-insecure-requests"="1"
)
#除了cookie 和:的其他丟進來
curl_handle <- getCurlHandle()
curlSetOpt(.opts = list(myHttpHeader), cookiejar="cookies.txt",  useragent = ua, followlocation = TRUE, curl=curl_handle, verbose = TRUE)

data <- list()
i <- 1
for( link in rss$item_link ){
  print( paste(i, link, sep=","))
  html_doc <- htmlParse(getURL(link, curl = curl_handle), encoding = "UTF-8")
  article_item <- xpathSApply(html_doc, '//*[@id="story_body_content"]//p', xmlValue)###這邊要去看xpath怎麼用
  article_item <- gsub("\\s+", "", article_item)##  S=>空白  \\跳脫 +多個
  article_item <- gsub(" $", "", article_item)##空白結尾
  article_item <- paste(article_item, collapse = " ") 
  data[i] <- article_item
  i <- i+1
  t <- sample(2:5,1)#隨機 T
  Sys.sleep(t)#休息T秒
}
data <- unlist(data)
data
###進行分詞
cutter= worker()
seg_words<- cutter <= data
#####計算每個字的出現頻率
#方法一 
library(plyr) 
table_words <- count(seg_words)#計算字

#方法二 在R使用SQL語法 
install.packages("sqldf") 
library(sqldf) 
seg_words1 <- as.data.frame(x = seg_words) 
table_words <- sqldf("SELECT seg_words,count(*) FROM seg_words1 group by seg_words")

# 繪製文字雲
library(wordcloud2) 
wordcloud2(table_words,color = "random-light",backgroundColor = "white")#繪製文字雲
