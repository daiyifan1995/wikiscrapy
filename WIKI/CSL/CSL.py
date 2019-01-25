from download import downloadhtml,writeurl
from openhtml import openhtml,openurl
from AnalyseHtml.getUrl import structUrls
from urllib.parse import unquote
from AnalyseHtml.InfoBox import getInforbox
from AnalyseHtml.Brief import getBrief,getBrief2
from AnalyseHtml.AttendTeams import getAttendteams4,getAttendteams3
from UrlFromHtml import geturlfromhtml
from WritetoJson import writejson
import re


#downloadhtml("中国足球协会超级联赛","CSL/中超.txt","w")
# soup=openhtml("CSL/中超.txt")[0]
# urls=structUrls(soup,"历届冠军")
# writeurl(urls,"CSL/URLS.txt")
# urls=openurl("CSL/URLS.txt")
# for url in urls:
#     url = url.replace("https://zh.wikipedia.org/wiki/", "")
#     downloadhtml(url,"CSL/中超HTML.txt","a")
htmls=openhtml("CSL/中超HTML.txt")
htmls.append(openhtml("CSL/中超.txt")[0])
# for i in htmls:
#     print(i.title)

for i in range(0,len(htmls)):
    dict = {"name": "", "link": "", "brief": "", "Inforbox": ""}#"attendteams": "",

    soup=htmls[i]

    url=geturlfromhtml(soup)
    dict["link"]=url

    name=soup.select("title")[0].get_text().replace(" - 维基百科，自由的百科全书","")
    dict["name"]=name

    infobox=getInforbox(soup)
    dict["Inforbox"]=infobox

    brief=getBrief(soup).strip("\n")
    if brief=="":
        brief=getBrief2(soup).strip("\n")
    dict["brief"]=brief

    if i<len(htmls)-1:
        attendteams = []
        try:#getAttendteams4和3的顺序不能颠倒
            attendteams = getAttendteams4(soup,"积分榜","積分榜")

            print(url, attendteams)
        except:
            attendteams = getAttendteams3(soup,"积分榜","積分榜")
            print(url,attendteams)
        dict["attendteams"]=attendteams

    writejson(dict, "CSL/中超_output.json")