import json

def writejson(dict,filename,append="a"):
    with open(filename,append, encoding="utf-8") as js:
        json.dump(dict, js,ensure_ascii=False)  # 只能写入字典
        js.write('\n')  # 可以换行