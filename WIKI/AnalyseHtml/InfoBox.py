import re

#wiki的inforbox
def getInforbox(soup):
    inforbox=[]
    if len(soup.select("table.infobox"))!=0:
        information = soup.select("table.infobox")[0].select("tr")
        for i in information:
            try:
                title = str(i.select("th")[0])
                content = str(i.select("td")[0])
            except:
                if len(i.select("img")) != 0:
                    img=i.select("img")[-1]
                    img=re.search("src=\".*?\"",str(img))

                    infor = {"Img": img.group()}
                    if img.group()!="src=\"//upload.wikimedia.org/wikipedia/commons/thumb/c/ce/Soccerball_current_event.svg/33px-Soccerball_current_event.svg.png\"":
                        inforbox.append(infor)#去掉足球的照片
                continue
            title = re.sub("<.*?>", " ", title)
            content = re.sub("<.*?>", " ", content)
            infor = {title: content}
            inforbox.append(infor)
    return inforbox
