import urllib.request
from bs4 import BeautifulSoup

def openhtml(filename):
    soups=[]
    with open(filename,"r",encoding="utf-8")as f1:
        soup=f1.readlines()
        for i in soup:
            i=BeautifulSoup(i)
            soups.append(i)
    return soups

def openurl(filename):
    urls=[]
    with open(filename,"r",encoding="utf-8")as f1:
        url=f1.readlines()
        for i in url:
            i=i.strip("\n")
            urls.append(i)
    return urls

