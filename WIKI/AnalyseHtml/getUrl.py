from urllib.parse import unquote
import re

def structUrls(soup,id):

    urls=[]
    tables = soup.findAll(name='span', attrs={"id": re.compile(r'%s'%id)})[0].parent.next_siblings
    for i in tables:
        if i.name == "table":
            table = i
            break
        else:
            continue
    cols = table.select("tr")
    for col in cols:
        if(len(col.select("td"))==0):
            continue
        col=col.select("td")[0]
        if col.select("a") != []:
            i = col.select("a")[0]
            link_suffix = unquote(i.attrs["href"])
            url= "https://zh.wikipedia.org" + link_suffix
            urls.append(url)
    return urls

def structUrls1(soup,id):

    urls=[]
    tables = soup.findAll(name='span', attrs={"id": re.compile(r'%s'%id)})[0].parent.next_siblings
    for i in tables:
        if i.name == "table":
            table = i
            break
        else:
            continue
    cols = table.select("tr")
    for col in cols:
        if(len(col.select("td"))==0):
            continue
        col=col.select("td")[0]
        if col.select("a") != []:
            i = col.select("a")[0]
            link_suffix = unquote(i.attrs["href"])
            url= "https://zh.wikipedia.org" + link_suffix
            urls.append(url)
    return urls