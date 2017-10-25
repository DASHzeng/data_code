library(RCurl)
library(rjson)

getmoviedata <- function(){
  i<- 1
  a<-data.frame()
  while(TRUE){
    url1<-'http://www.cbooo.cn/BoxOffice/getInland?pIndex='
    url2<-'&t=0'
    url3=paste0(url1,i,url2)
    res<-getURL(url3)
    
    if(res==''){
      break
    }
    j<-fromJSON(res)
    d<-as.data.frame.factor(j)
    for (x in 1:20){
      o<-as.data.frame(d$j[[x]])
      a<-rbind(a,o)
      }
    }
    i<-i+1
  }
  return(a)
}

  
ttt<-getmoviedata()


