from sdk.other import Main as other
from mod.mods.content.content import AliasSearchContent
from mod.mods.content.ORSCFS import content as ORSCFScontent
import json
class URL():
    def __init__(self) -> None:
        '''
        This class is instantiated in mian.py and will automatically obtain the configuration. 
        If needed, GetURLTemplate() can be used to retrieve the configuration again
        '''
        self.OT = other('UrlTemplate')

    def GetURLTemplate(self):
        self.OT.Pulling()
        if (self.OT.data == None):
            self.OT.data = {'content':"/<%^alias^%>.html",
                                     'classification':"/classification/<%^alias^%>.html"
                                     }
    def change(self,new):
        self.OT.data = new
        self.OT.SubmitToDatabase()
    def coverR(self,url:str):
        '''Apply the template and return the corresponding content'''
        for k,v in self.OT.data.items():
            o = v.split('<%^')[0]
            n = v.split('^%>')[-1]
            if (url[:(len(o))] == o and url[-len(n):] == n):
                urlContent = url.translate({ord(letter): None for letter in [o,n]})
                if (k == 'content'):
                    content = AliasSearchContent(urlContent)
                    content['content'] = ORSCFScontent(content['content']).html()
                    return json.dumps(content)
                
        return ''