from openhtml import openhtml,openurl
from urllib.parse import unquote
from UrlFromHtml import geturlfromhtml
from WritetoJson import writejson
import re
from download import downloadhtml,writeurl
from openhtml import openhtml,openurl
from AnalyseHtml.getUrl import structUrls,structUrls1
from AnalyseHtml.InfoBox import getInforbox
from AnalyseHtml.Brief import getBrief,getBrief2
from AnalyseHtml.AttendTeams import  getAttendteams,getAttendteams2
from UrlFromHtml import geturlfromhtml
from WritetoJson import writejson




#downloadhtml("英格兰足球超级联赛","ENgland/英格兰足球超级联赛.txt","w")
#soup=openhtml("ENgland/英格兰足球超级联赛.txt")[0]
#urls=structUrls(soup,"歷屆冠軍")
# writeurl(urls,"ENgland/urls.txt")
# urls=openurl("ENgland/urls.txt")
# for url in urls:
# print(url)
# url=url.replace("https://zh.wikipedia.org/wiki/","")
# print(url)
# downloadhtml(url, "ENgland/英超.txt","a")
htmls=openhtml("ENgland/英超.txt")
initial=openhtml("ENgland/英格兰足球超级联赛.txt")[0]
htmls.append(initial)

soup=htmls[-1]

for i in range(0,len(htmls)):
    dict = {"name": "", "link": "", "brief": "", "Inforbox": ""}  # "attendteams": "",

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
        try:#getAttendteams2和2的顺序不能颠倒
            attendteams = getAttendteams2(soup,"積分榜")

            print(url, attendteams)
        except:
            attendteams = getAttendteams(soup,"積分榜")
            print(url,attendteams)
        dict["attendteams"]=attendteams

    writejson(dict,"ENgland/英超_output.json")
