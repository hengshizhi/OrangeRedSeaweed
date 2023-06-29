# The content module of OrangeRedSeaweed is mainly used to handle website content
# Belongs to the official module of OrangeRedSeaweed
# Copyright 2023 Starweave
from mod.mods.content.AtRuntimeForTheFirstTime import AtRuntimeForTheFirstTime as AtRuntimeForTheFirstTime
import json
def main(api):
    api['GetAllContentTemplates'] = GetAllContentTemplatesAPI
    api['NewContent'] = NewContentApi
    return api

def GetAllContentTemplatesAPI(get_or_post,EnableSession,rep,**para):
    from mod.mods.content.ORSCFS import ContentTemplate as ContentTemplates 
    return rep(json.dumps(ContentTemplates))

def NewContentApi(get_or_post,EnableSession,rep,**para):
    import sdk.other as other
    s = EnableSession()
    if (not other.ValidateLogon(s)[0]):return rep('No Logon')
    OT = other.Main('CoreConfiguration',session=s)
    OT.Pulling()
    return rep(str(OT.data))
