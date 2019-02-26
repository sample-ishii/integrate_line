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
    
    @classmethod
    def getResponse(response,text):
        if response.count>=4:
            response.count=0
        response.count+=1
        for _dic in response.dic:
            if _dic==text:
                return response.dic[text]
        return Response.count

