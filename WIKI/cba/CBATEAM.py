import json
import urllib.request
from bs4 import BeautifulSoup
import re
from urllib.parse import unquote

def getteamUrl(filename):
    teamUrl=set()
    with open(filename,"r",encoding="utf-8") as js1:
        a=js1.read()
        for i in a.split("\n"):
            try:
                dict=json.loads(i)
                teams=dict["attendteams"]
                for team in teams:
                    url=team["link"]
                    teamUrl.add(url)
            except:
                continue
    return teamUrl

def getInforbox(url,soup):
    inforbox={}
    if len(soup.select("table[align='right']"))!=0:
        table = soup.select("table[align='right']")[0]
        try:
            elments = table.select("tr")
            for i in elments:
                if i.select("img")!=[] and "teamImg" not in inforbox.keys():
                    img=i.select("img")[0]
                    img = re.search("src=\".*?\"", str(img))
                    inforbox["teamImg"]=img.group()
                if len(i.select("td"))==2:
                    title=re.sub("<.*?>","",str(i.select("td")[0]))
                    content=re.sub("<.*?>","",str(i.select("td")[1]))
                    inforbox[title]=content
        except:
            inforbox["ERROr"]=url
    elif len(soup.select("table[class='infobox vcard']"))!=0:
        elments = soup.select("table.infobox")[0].select("tr")
        for i in elments:
            if i.select("img") != [] and len(i.select("td")) ==0:
                img = i.select("img")[0]
                img = re.search("src=\".*?\"", str(img))
                inforbox["teamImg"] = img.group()
            if len(i.select("td")) !=0 and len(i.select("th")) !=0:
                title = re.sub("<.*?>", "", str(i.select("th")[0]))
                content = re.sub("<.*?>", "", str(i.select("td")[0]))
                inforbox[title] = content

    return inforbox

def parseTeam(url):
    team={}

    team["url"]=url

    html = urllib.request.urlopen(url=url).read().decode("utf-8")
    soup = BeautifulSoup(html)

    team["teamName"]=soup.title.get_text().split("-")[0]
    if "创建" in team["teamName"]:
        team["infobox"]="wiki暂无该词条"
    else:
        team["infobox"]=getInforbox(url,soup)

    print(team)



    return team

#parseTeam("https://zh.wikipedia.org/wiki/"
          #"%E5%8C%97%E4%BA%AC%E6%8E%A7%E8%82%A1%E7%BF%B1%E9%BE%99%E7%AF%AE%E7%90%83%E4%BF%B1%E4%B9%90%E9%83%A8")
for url in getteamUrl("cba_zh.json"):
    parseTeam(url)

