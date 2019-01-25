import urllib.request
from bs4 import BeautifulSoup
from urllib.parse import quote

#下载html文件，url不带域名
def downloadhtml(url,filename,append,domainName="https://zh.wikipedia.org/wiki/",):
    url=domainName+quote(url, safe='')
    html = urllib.request.urlopen(url=url).read().decode("utf-8")
    soup = BeautifulSoup(html)
    soup=str(soup)
    #soup=soup.replace("\r\n","")
    #soup =soup.replace("\n","")
    f=open(filename,append,encoding="utf-8")
    f.write(soup)
    f.write("\n")
    f.close()

def writeurl(urls,filename,append="w"):
    with open(filename,append,encoding="utf-8")as f1:
        for url in urls:
            f1.write(url)
            f1.write("\n")

downloadhtml("2018年亞足聯冠軍聯賽","test.txt","w")
