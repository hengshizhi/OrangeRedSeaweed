import sdk.other as other
import time
# import json
import uuid
from mod.mods.content.ORSCFS import content as ORSCFS

class content():
    GenerateStorage = lambda self,Title,alias,content:{"title": Title, "alias": alias,"Release": time.time(),"change": [time.time(),],"ORSCFS": content}
    def __init__(self,session,Title = None,alias = None,content:list([dict({'name':'模板名称','...':'...'}),'...']) = None) -> None:
        '''
        parameter :session : session object         
            Title,alias :内容标题,别名
            content :ORSCFS 格式的内容
        '''
        self.OT = other.Main('ContentList',session=session)
        if (alias == None):
            if (Title == None):
                self.Title = 'None'
            if (alias == None):
                self.alias = str(uuid.uuid4())
            self.content = content
        else:
            self.Title = Title
            self.alias = alias
            self.content = content
        self.Pulling()
    def new(self):
        '''新建内容'''
        try:
            self.OT.data['main'].append({self.GenerateStorage(self.Title, self.alias, self.content)})
        except:
            self.OT.data = {'main':None}
            self.OT.data['main'] = [self.GenerateStorage(self.Title,self. alias,self. content),]
    def AliasLookup(self):
        '''根据别名查找内容在内容列表的位置'''
        for i in range (len(self.OT.data['main'])):
            if (self.OT.data['main'][i]['alias'] == self.alias):
                return i
        return None # 内容不存在
    def change(self):
        AliasLookup = self.AliasLookup()
        self.OT.data['main'][AliasLookup]['Title'] = self.Title
        self.OT.data['main'][AliasLookup]['alias'] = self.alias
        self.OT.data['main'][AliasLookup]['content'] = self.content
        self.OT.data['main'][AliasLookup]['change'].append(time.time())
    def SubmitToDatabase(self):
        self.OT.SubmitToDatabase() # 提交
    def Pulling(self):
        self.OT.Pulling()
        AliasLookup = self.AliasLookup()
        self.content = self.OT.data['main'][AliasLookup]['content']
        self.Title = self.OT.data['main'][AliasLookup]['Title']
    def read(self):
        '''读取,返回html'''
        OSF = ORSCFS(self.content)
        return OSF.html()