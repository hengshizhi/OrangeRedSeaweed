import sdk.other as other
import time
import json
class content():
    def __init__(self,user_id) -> None:
        '''
        parameter :user_id :用户id
        '''
        self.user_id = user_id
        pass
    def new(self,Title, alias, content :list([dict({'name':'模板名称','...':'...'}),'...']),):
        '''新建内容
        parameter :
            Title,alias :内容标题,别名
            content :ORSCFS 格式的内容
            
        '''
        LimitsOfAuthority = other.CoreConfiguration(self.user_id)
        if (LimitsOfAuthority.administrators or LimitsOfAuthority.ContentEditingRights):
            O = other.Main(KEY='ContentList',ID=self.user_id)
            del LimitsOfAuthority
    
    