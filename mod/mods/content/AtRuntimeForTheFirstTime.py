import fileApi.route as route
import fileApi.PathInfo as PathInfo
import json
def AtRuntimeForTheFirstTime():
    ''' Functions that will be executed every time the program runs mod '''
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
