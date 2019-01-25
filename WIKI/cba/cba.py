import urllib.request
from urllib.parse import quote
from bs4 import BeautifulSoup
from urllib.parse import unquote
from InfoBox import getInforbox
from Brief import getBrief,getBrief2
from WritetoJson import writejson
import re

#参赛球队
def getAttendteams(time,soup):
    attendteams=[]
    try:
        tables = soup.findAll(name='span',attrs={"id":re.compile(r'常规赛')})[0].parent.next_siblings
        for i in tables:
            if i.name=="table":
                table=i
                break
            else:
                continue
        cols=table.select("td")
        for col in cols:
            team={}
            if col.select("a")!=[]:
                i=col.select("a")[0]
                link_suffix=unquote(i.attrs["href"])
                team["link"]="https://zh.wikipedia.org"+link_suffix
                print(team["link"])
                team["fullName"] = i.attrs["title"]
                team["name"] = i.text
                attendteams.append(team)
            else:
                continue
        return attendteams
    except:
        attendteams.append(time)
        return attendteams

#08-09年北区
def getAttendteams2(time,soup):
    attendteams=[]
    try:
        elements = soup.findAll(name='span',attrs={"id":re.compile(r'参赛球队')})[0].parent.next_siblings
        tables=[]
        j=0
        for i in elements:
            if i.name=="table":
                tables.append(i)
                j=j+1
                if j==2:
                    break
            else:
                continue
        for table in tables:
            cols=table.select("th")
            for col in cols:
                team={}
                if col.select("a")!=[]:
                    i=col.select("a")[0]
                    link_suffix = unquote(i.attrs["href"])
                    team["link"] = "https://zh.wikipedia.org" + link_suffix
                    team["fullName"] = i.attrs["title"]
                    team["name"] = i.text
                    attendteams.append(team)
                else:
                    continue
        return attendteams
    except:
        attendteams.append(time)
        return attendteams

#18-19年人事及赞助
def getAttendteams3(time,soup):
    attendteams=[]
    try:
        tables = soup.findAll(name='span',attrs={"id":re.compile(r'人事及赞助')})[0].parent.next_siblings
        for i in tables:
            if i.name=="table":
                table=i
                break
            else:
                continue
        cols=table.select("tbody")[0].select("tr")
        for col in cols:
            team={}
            if col.select("td")!=[]:
                col=col.select("td")[0]
                if col.select("a")!=[]:
                    i=col.select("a")[0]
                    link_suffix = unquote(i.attrs["href"])
                    team["link"] = "https://zh.wikipedia.org" + link_suffix
                    team["fullName"] = i.attrs["title"]
                    team["name"] = i.text
                    attendteams.append(team)
        return attendteams
    except:
        attendteams.append(time)
        return attendteams

#05-06常规赛成绩
def getAttendteams4(time,soup):
    attendteams=[]
    try:
        elements = soup.findAll("b",text=re.compile(r'北区|南区'))[0].parent.next_siblings
        tables=[]
        j=0
        for i in elements:
            if i.name=="table":
                table=i
                j=j+1
                tables.append(table)
                if j==2:
                    break
            else:
                continue
        for table in tables:
            cols=table.select("tbody")[0].select("tr")
            for col in cols:
                team={}
                if col.select("td")!=[]:
                    col=col.select("td")[0]
                    if col.select("a")!=[]:
                        i=col.select("a")[0]
                        link_suffix = unquote(i.attrs["href"])
                        team["link"] = "https://zh.wikipedia.org" + link_suffix
                        team["fullName"] = i.attrs["title"]
                        team["name"] = i.text
                        attendteams.append(team)
        return attendteams
    except:
        attendteams.append(time)
        return attendteams

#解析cba网页
def parseCba(time,url):
    game={"name":"","link":"","attendteams":"","brief":"","Inforbox":""}

    if time != "":
        game["name"]=str(time)+"年中国男子篮球职业联赛"
    else:
        game["name"] = "中国男子篮球职业联赛"

    if time!="":
        game["link"]="https://zh.wikipedia.org/wiki/"+str(time)+"年中国男子篮球职业联赛"
    else:
        game["link"] = "https://zh.wikipedia.org/wiki/中国男子篮球职业联赛"

    html = urllib.request.urlopen(url=url).read().decode("utf-8")
    soup = BeautifulSoup(html)

    if time!="":
        attendteams = getAttendteams(time, soup)
        if time == "2008-09":
            attendteams = getAttendteams2(time, soup)#08-09
        if time == "2018-19" or time=="2016-17":#16-17的常规赛数据为个人数据
            attendteams = getAttendteams3(time, soup)#18-19
        if time == "2005-06":
            attendteams = getAttendteams4(time, soup)#05-06
        game["attendteams"] = attendteams

    Inforbox = getInforbox(soup)
    game["Inforbox"]=Inforbox

    brief = getBrief(soup)
    game["brief"]=brief

    return game

urls=[]#cba的url信息
for i in range(5,20):
    j=i+1
    if i==19:
        time=""
    else:
        time="20%02d-%02d年"%(i,j)
    url=str(time)+"中国男子篮球职业联赛"
    url="https://zh.wikipedia.org/wiki/"+quote(url, safe='')
    urls.append(url)
    game=parseCba(time,url)
    writejson(dict,"cba_output.json","a")



