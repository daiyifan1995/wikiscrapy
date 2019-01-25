import json

def Readfromjson(filename):
    strs=[]
    with open("AFC/亚冠_output.json", "r", encoding="utf-8") as js1:
        a = js1.read()

    for i in a.split("\n"):
        strs.append(i)

    return  strs