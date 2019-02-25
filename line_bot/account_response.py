# -*- coding: utf-8 -*-

import random

dic={"会社概要":"COMPANY", "事業内容":"SERVICE", "採用情報":"CAREER", "コマンド":"COMMAND"}

def getResponse(self,text):
    
    for _dic in dic:
        if _dic==text:
            return dic[text]
    
    return random.randint(1,3)

