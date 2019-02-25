# -*- coding: utf-8 -*-


dic={"会社概要":"COMPANY",
     "事業内容":"SERVICE",
     "採用情報":"CAREER",
     "コマンド":"COMMAND",
     "おはよう":"5",
     "こんにちは":"5",
     "こんばんは":"5",
     "こんにちわ":"6",
     "こんばんわ":"6"
     }
count=0

def getResponse(self,text):
    global count
    if count>=4:
        count=0
    count+=1
    for _dic in dic:
        if _dic==text:
            return dic[text]
    return count

