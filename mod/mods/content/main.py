# The content module of OrangeRedSeaweed is mainly used to handle website content
# Belongs to the official module of OrangeRedSeaweed
# Copyright 2023 Starweave
import fileApi.route as route
import fileApi.PathInfo as PathInfo
import json

def main(api):
    api['GetContentTemplates'] = GetContentTemplates
    return api

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

def GetContentTemplates(get_or_post,EnableSession,rep,**para):
    from mod.mods.content.ORSCFS import ContentTemplate as ContentTemplates 
    print(ContentTemplates) 
    return rep(json.dumps(ContentTemplates))