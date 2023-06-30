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
    s = EnableSession()
    import sdk.other as other
    LimitsOfAuthority = other.CoreConfiguration(session=s)
    if (LimitsOfAuthority.administrators or LimitsOfAuthority.ContentEditingRights):
        del LimitsOfAuthority
        from mod.mods.content.content import content as content_obj
        Title,alias,content = get_or_post('alias'),get_or_post('Title'),get_or_post('content')
        con = content_obj(session=s,Title=Title,alias=alias,content=content)
        con.SubmitToDatabase()
        return rep('OK')
    else:
        del LimitsOfAuthority
        return rep('No use authority')
