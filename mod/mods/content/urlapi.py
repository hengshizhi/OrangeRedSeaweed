from sdk.other import Main as other
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
                url = url.translate({ord(letter): None for letter in [o,n]})
                if (k == 'content'):
                    pass