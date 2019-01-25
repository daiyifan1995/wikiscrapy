from langconv import *
from ReadfromJson import Readfromjson
from WritetoJson import writejson
import json

def Traditional2Simplified(sentence):
    '''
    将sentence中的繁体字转为简体字
    :param sentence: 待转换的句子
    :return: 将句子中繁体字转换为简体字之后的句子
    '''
    sentence = Converter('zh-hans').convert(sentence)
    return sentence

if __name__=="__main__":
    strs=Readfromjson("AFC/亚冠_output.json")
    for i in strs:
        traditional_sentence = i
        simplified_sentence = Traditional2Simplified(traditional_sentence)
        try:
            simplified_sentence=json.loads(simplified_sentence,encoding="utf-8")
            writejson(simplified_sentence,"AFC/亚冠_output(简).json","a")
        except:
            print(simplified_sentence)


