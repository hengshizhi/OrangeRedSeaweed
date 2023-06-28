# The content module of OrangeRedSeaweed is mainly used to handle website content
# Belongs to the official module of OrangeRedSeaweed
# Copyright 2023 Starweave
from mod.mods.content.AtRuntimeForTheFirstTime import AtRuntimeForTheFirstTime as AtRuntimeForTheFirstTime

def main(api):
    api['GetAllContentTemplates'] = GetAllContentTemplatesAPI
    api['NewContent'] = NewContent
    return api

def GetAllContentTemplatesAPI(get_or_post,EnableSession,rep,**para):
    from mod.mods.content.ORSCFS import ContentTemplate as ContentTemplates 
    return rep(json.dumps(ContentTemplates))

