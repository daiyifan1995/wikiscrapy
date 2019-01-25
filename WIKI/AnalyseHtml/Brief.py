import re

#wiki的brief
def getBrief(soup):
    brief=""
    ##mw-content-text > div > p:nth-child(3)
    soup=soup.select("div[id='mw-content-text']")[0]
    if len(soup.select("div[id='toc']"))!=0:
        briefs = soup.select("div[id='toc']")[0].previous_siblings
        brief=""
        for i in briefs:
            if i.name=="p":
                brief = re.sub("<.*?>", "", str(i))+"\n"+brief
                continue
                if i.name!="p":
                    break
    return brief

#无导航的brief
def getBrief2(soup):
    brief=""
    ##mw-content-text > div > p:nth-child(3)
    soup=soup.select("div[id='mw-content-text']")[0]
    if len(soup.select("table[class='infobox']"))!=0:
        briefs = soup.select("table[class='infobox']")[0].next_siblings
        brief=""
        for i in briefs:
            if i.name=="p":
                brief = brief+"\n"+re.sub("<.*?>", "", str(i))
                continue
                if i.name!="p":
                    break
    return brief