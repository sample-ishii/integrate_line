# -*- coding: utf-8 -*-

class Response:
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
        if Response.count>=4:
            Response.count=0
        Response.count+=1
        for _dic in self.dic:
            if _dic==text:
                return self.dic[text]
        return Response.count

