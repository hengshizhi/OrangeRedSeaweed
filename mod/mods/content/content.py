import sdk.other as other
import time
import json
def new(Title, alias, content :list([dict({'name':'模板名称','...':'...'}),'...']),user_id):
    '''新建内容
    parameter :
        Title,alias :内容标题,别名
        content :ORSCFS 格式的内容
        user_id :用户id
    '''
    O = other.Main(KEY='ContentList',ID=user_id)
    contents = 
    