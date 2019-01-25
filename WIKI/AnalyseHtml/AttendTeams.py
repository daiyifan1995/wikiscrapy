import re
from urllib.parse import unquote


def getAttendteams(soup,id):
    attendteams=[]

    tables = soup.findAll(name='span',attrs={"id":re.compile(r'%s'%id)})[0].parent.next_siblings
    for i in tables:
        if i.name=="table":
            table=i
            break
        else:
            continue
    if len(table.select("tr"))!=0:
        cols = table.select("tr")
        for col in cols:
            if col.select("td") != []:
                col = col.select("td")[1]
                team = {}
                if col.select("a")!=[]:
                    i=col.select("a")[0]
                    link_suffix=unquote(i.attrs["href"])
                    team["link"]="https://zh.wikipedia.org"+link_suffix
                    team["fullName"] = i.attrs["title"]
                    team["name"] = re.sub("<.*?>", "", str(i))
                    attendteams.append(team)
        if attendteams==[]:
            cols = table.select("tr")
            for col in cols:
                if col.select("td") != []:
                    col = col.select("td")[0]
                    team = {}
                    if col.select("a") != []:
                        i = col.select("a")[0]
                        link_suffix = unquote(i.attrs["href"])
                        team["link"] = "https://zh.wikipedia.org" + link_suffix
                        team["fullName"] = i.attrs["title"]
                        team["name"] = re.sub("<.*?>", "", str(i))
                        attendteams.append(team)

    return attendteams
    # else:
    #     cols=table.select("td")
    #     for col in cols:
    #         team={}
    #         if col.select("a")!=[]:
    #             i=col.select("a")[0]
    #             link_suffix=unquote(i.attrs["href"])
    #             team["link"]="https://zh.wikipedia.org"+link_suffix
    #             team["fullName"] = i.attrs["title"]
    #             team["name"] = re.sub("<.*?>", "", str(i))
    #             attendteams.append(team)
    #     return attendteams



def getAttendteams2(soup,id):
    attendteams=[]
    tables = soup.findAll(name='span',attrs={"id":re.compile(r'%s'%id)})[0].parent.next_siblings
    for i in tables:
        if i.name=="div":
            table = i.findAll(name='table', attrs={"class": re.compile(r'wikitable')})[0]
            break
        else:
            continue
    cols=table.select("tr")
    for col in cols:
        if len(col.select("td"))>1:
            col=col.select("td")[1]
            team={}
            if col.select("a")!=[]:
                i=col.select("a")[0]
                link_suffix=unquote(i.attrs["href"])
                team["link"]="https://zh.wikipedia.org"+link_suffix
                team["fullName"] = i.attrs["title"]
                team["name"] = re.sub("<.*?>","",str(i))
                attendteams.append(team)
    return attendteams

#3是getAttendteams的拓展，有两中id名，id名之间是或的关系
def getAttendteams3(soup,id,id2):
    attendteams=[]
    tables = soup.findAll(name='span',attrs={"id":re.compile(r'%s|%s'%(id,id2))})[0].parent.next_siblings
    for i in tables:
        if i.name=="table":
            table=i
            break
        else:
            continue
    if len(table.select("tr"))!=0:
        cols = table.select("tr")
        for col in cols:
            if col.select("td") != []:
                col = col.select("td")[1]
                team = {}
                if col.select("a")!=[]:
                    i=col.select("a")[0]
                    link_suffix=unquote(i.attrs["href"])
                    team["link"]="https://zh.wikipedia.org"+link_suffix
                    team["fullName"] = i.attrs["title"]
                    team["name"] = re.sub("<.*?>", "", str(i))
                    attendteams.append(team)
        if attendteams==[]:
            cols = table.select("tr")
            for col in cols:
                if col.select("td") != []:
                    col = col.select("td")[0]
                    team = {}
                    if col.select("a") != []:
                        i = col.select("a")[0]
                        link_suffix = unquote(i.attrs["href"])
                        team["link"] = "https://zh.wikipedia.org" + link_suffix
                        team["fullName"] = i.attrs["title"]
                        team["name"] = re.sub("<.*?>", "", str(i))
                        attendteams.append(team)

    return attendteams


def getAttendteams4(soup,id,id2):
    attendteams=[]
    tables = soup.findAll(name='span',attrs={"id":re.compile(r'%s|%s'%(id,id2))})[0].parent.next_siblings
    for i in tables:
        if i.name=="div":
            table = i.findAll(name='table', attrs={"class": re.compile(r'wikitable')})[0]
            break
        else:
            continue
    cols=table.select("tr")
    for col in cols:
        if len(col.select("td"))>1:
            col=col.select("td")[1]
            team={}
            if col.select("a")!=[]:
                i=col.select("a")[0]
                link_suffix=unquote(i.attrs["href"])
                team["link"]="https://zh.wikipedia.org"+link_suffix
                team["fullName"] = i.attrs["title"]
                team["name"] = re.sub("<.*?>","",str(i))
                attendteams.append(team)
    return attendteams

#3在增加了去重功能后，两个表格的模式分块成了5和5_b
#5是getAttendteams3的拓展，有2个id名，需要去重
def getAttendteams5(soup,id,id2):
    attendteams=[]
    linkset=set()
    spans=soup.findAll(name='span',attrs={"id":re.compile(r'%s|%s'%(id,id2))})
    for span in spans:
        tables = span.parent.next_siblings
        for i in tables:
            if i.name=="table":
                table=i
                break
            else:
                continue
        if len(table.select("tr"))!=0:
            cols = table.select("tr")
            for col in cols:
                if col.select("td") != []:
                    col = col.select("td")[0]
                    team = {}
                    if col.select("a") != []:
                        i = col.select("a")[1]
                        link_suffix = unquote(i.attrs["href"])
                        if link_suffix not in linkset:
                            linkset.add(link_suffix)
                            if "2009年亞足聯冠軍聯賽小組賽" in link_suffix:
                                continue
                            team["link"] = "https://zh.wikipedia.org" + link_suffix
                            if "title" in str(i):
                                team["fullName"] = i.attrs["title"]
                            else:
                                team["fullName"]=link_suffix
                            team["name"] = re.sub("<.*?>", "", str(i))
                            attendteams.append(team)
    return attendteams
#5_b是getAttendteams5的另外一部分，表格格式为每行前加了一个序号
def getAttendteams5_b(soup,id,id2):
    attendteams=[]
    linkset=set()
    spans=soup.findAll(name='span',attrs={"id":re.compile(r'%s|%s'%(id,id2))})
    for span in spans:
        tables = span.parent.next_siblings
        for i in tables:
            if i.name=="table":
                table=i
                break
            else:
                continue
        if len(table.select("tr"))!=0:
            cols = table.select("tr")
            for col in cols:
                if col.select("td") != []:
                    col = col.select("td")[1]
                    team = {}
                    if col.select("a")!=[]:
                        i=col.select("a")[1]
                        link_suffix=unquote(i.attrs["href"])
                        if link_suffix not in linkset:
                            linkset.add(link_suffix)
                            team["link"]="https://zh.wikipedia.org"+link_suffix
                            team["fullName"] = i.attrs["title"]
                            team["name"] = re.sub("<.*?>", "", str(i))
                            attendteams.append(team)

    return attendteams
#5_c是getAttendteams5的另外一部分，表格格式为两个表格合成一个表格
def getAttendteams5_c(soup,id,id2):
    attendteams=[]
    linkset=set()
    spans=soup.findAll(name='span',attrs={"id":re.compile(r'%s|%s'%(id,id2))})
    for span in spans:
        tables = span.parent.next_siblings
        for i in tables:
            if i.name=="table":
                table=i
                break
            else:
                continue
        if len(table.select("tr"))!=0:
            cols = table.select("tr")[0]
            cols=cols.select("td")
            for col in cols:
                elments=col.select("tr")
                for elment in elments:
                    if len(elment.select("td"))>0:
                        col = elment.select("td")[0]
                        team = {}
                        if len(col.select("a"))>=2:
                            i = col.select("a")[1]
                            link_suffix = unquote(i.attrs["href"])
                            if link_suffix not in linkset:
                                linkset.add(link_suffix)
                                if "2009年亞足聯冠軍聯賽小組賽" in link_suffix:
                                    continue
                                team["link"] = "https://zh.wikipedia.org" + link_suffix
                                if "title" in str(i):
                                    team["fullName"] = i.attrs["title"]
                                else:
                                    team["fullName"]=link_suffix
                                team["name"] = re.sub("<.*?>", "", str(i))
                                attendteams.append(team)
    return attendteams


#6是getAttendteams5的拓展，有2个id名，有2列，需要去重
def getAttendteams6(soup,id,id2):
    attendteams=[]
    linkset=set()
    spans=soup.findAll(name='span',attrs={"id":re.compile(r'%s|%s'%(id,id2))})
    for span in spans:
        tables = span.parent.next_siblings
        for i in tables:
            if i.name=="table":
                table=i
                break
            else:
                continue
        if len(table.select("tr"))!=0:
                cols = table.select("tr")
                for col in cols:
                    length=len(col.select("td"))
                    row=0
                    while  row<3 and  row<length:
                        item = col.select("td")[row]
                        team = {}
                        row = row + 2
                        if len(item.select("a"))>=2 :
                            if item.select("a")[0].parent.name!="span":
                                i=item.select("a")[0]
                            else:
                                i=item.select("a")[1]
                            link_suffix = unquote(i.attrs["href"])
                            if link_suffix not in linkset:
                                linkset.add(link_suffix)
                                team["link"] = "https://zh.wikipedia.org" + link_suffix
                                team["fullName"] = i.attrs["title"]
                                team["name"] = re.sub("<.*?>", "", str(i))
                                attendteams.append(team)

    return attendteams