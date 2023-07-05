import fileApi.route as route
import fileApi.PathInfo as PathInfo
import json
from InitialLoading import  Cache as Cache
from operation.user import Traverse_other_data_with_the_same_key_value
def AliasesCorrespondUsersID():
    ret = {}
    data = Traverse_other_data_with_the_same_key_value('ContentList')
    for k,v in data.items():
        for i in v['main']:
            ret[i['alias']] = k
    return ret
def AtRuntimeForTheFirstTime():
    ''' Functions that will be executed every time the program runs mod '''
    Cache.NewCache('AliasesCorrespondUsersID',AliasesCorrespondUsersID) # 储存缓存
    route.mkdir('./ContentTemplate')
    from mod.mods.content.ORSCFS import ContentTemplate as ContentTemplates 
    # 导入内容模板变量,储存内容模板
    # ContentTemplates = {
    #   '<Template file name (excluding suffix)>' = {
    #       json.loads()
    #   }
    # }
    for k,v in PathInfo.Dict('./ContentTemplate','./ContentTemplate').items(): # 遍历模板目录
        if('.ORStemplate.json' in k):
            with open(v[1],'r',encoding='utf-8') as template:
                ContentTemplates[k.replace('.ORStemplate.json','')] = json.loads(template.read())
