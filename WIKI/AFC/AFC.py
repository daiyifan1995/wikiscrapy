from download import downloadhtml,writeurl
from openhtml import openhtml,openurl
from AnalyseHtml.getUrl import structUrls,structUrls1
from AnalyseHtml.InfoBox import getInforbox
from AnalyseHtml.Brief import getBrief,getBrief2
from AnalyseHtml.AttendTeams import getAttendteams5,getAttendteams5_b,getAttendteams5_c,getAttendteams6
from UrlFromHtml import geturlfromhtml
from WritetoJson import writejson
from fantojian.Fan_ZHtoJian_ZH import Fantojian

# #获下载初始页面
# downloadhtml("亚足联冠军联赛","AFC/亚冠.txt","w")
# soup=openhtml("AFC/亚冠.txt")[0]

# #从初始页面获得全部url
# urls1=structUrls1(soup,"亞洲冠軍球會盃（Asian_Champion_Club_Tournament）")
# urls2=structUrls1(soup,"亞洲球會錦標賽（Asian_Club_Championship）")
# urls3=structUrls1(soup,"亞足聯冠軍聯賽（AFC_Champions_League）")
# urls_all=urls1+urls2+urls3
# #多层次的表需要将非年份的数据删掉

# urls=[]
# for url in urls_all:
#     if "年" in url:
#         print(url)
#         urls.append(url)
# writeurl(urls,"AFC/URLS.txt")

# #下载全部url的html文件
# urls=openurl("AFC/URLS.txt")
# for url in urls:
#     url = url.replace("https://zh.wikipedia.org/wiki/", "")
#     downloadhtml(url,"AFC/亚冠HTML.txt","a")


#打开全部html文件
htmls=openhtml("亚冠HTML.txt")
htmls.append(openhtml("亚冠.txt")[0])
# for i in htmls:
#     print(i.title)

#分析页面，将结果写入json
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
        attendteams = []#球队的连接并非都在b标签中
        if i==0:
            attendteams = getAttendteams6(soup, "第一","第二")
        elif i>=12 and i<=20:
            attendteams = getAttendteams6(soup, "亞","亞")
        else:
            try:
                attendteams = getAttendteams5(soup,"[A-Z].*組","[A-Z].*組")#仅计算小组赛(A,B,C,组),表格无序号为td
                if attendteams==[]:
                    attendteams = getAttendteams5_b(soup, "[A-Z].*組", "[A-Z].*組")#仅计算小组赛(A,B,C,组),表格有序号为td
                if attendteams==[]:
                    attendteams = getAttendteams5(soup, "組", "組")#无小组赛页面，计算第一、二组，表格无序号为td
                if attendteams==[]:
                    print(i)
                    attendteams = getAttendteams5_b(soup, "組", "組")#无小组赛页面，计算第一、二组，表格有序号为td
            except:
                    attendteams=getAttendteams5_c(soup, "[A-Z].*組", "[A-Z].*組")#一个表格中嵌套了两个表格


        dict["attendteams"]=attendteams
        print(i,url,len(attendteams),attendteams)
    writejson(dict,"亚冠_output.json","a")



# #若页面为繁体，转化为简体
# Fantojian("亚冠_output.json","亚冠_output(简).json","a")


