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
        self.GetURLTemplate()
    def GetURLTemplate(self):
        self.OT.Pulling()
        if (self.OT.data == {} or self.OT.data == None):
            self.OT.data = {'content':"/<%^alias^%>.html",
                                     'classification':"/classification/<%^alias^%>.html"
                                     }
            self.OT.SubmitToDatabase()
    def change(self,new):
        self.OT.data = new
        self.OT.SubmitToDatabase()
    def coverR(self,url:str):
        '''Apply the template and return the corresponding content'''
        url = url.replace('https:/','').replace('https:/','')
        print('url:',self.OT.data)
        for k,v in self.OT.data.items():
            o = v.split('<%^')[0]
            n = v.split('^%>')[-1]
            print('o:',o)
            print('n:',n)
            if (len(url[:(len(o))]) == len(o) and len(url[-len(n):]) == len(n)):
                urlContent = url.replace(o,'').replace(n,'')
                if (k == 'content'):
                    content = AliasSearchContent(urlContent)
                    content['content'] = ORSCFScontent(content['content']).html()
                    return json.dumps(content)
                
        return ''
    
URL = URL()
print('aaaaaaaaaaaaaaa'+ URL.coverR('https://5915040c-b758-4982-8a45-0c2c2ede2290.html'))