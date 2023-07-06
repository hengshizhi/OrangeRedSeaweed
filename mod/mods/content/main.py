# The content module of OrangeRedSeaweed is mainly used to handle website content
# Belongs to the official module of OrangeRedSeaweed
# Copyright 2023 Starweave
# from mod.mods.content.AtRuntimeForTheFirstTime import AtRuntimeForTheFirstTime as AtRuntimeForTheFirstTime
import json

from mod.mods.content.AtRuntimeForTheFirstTime import AtRuntimeForTheFirstTime
from mod.mods.content.content import content as content_obj
from mod.mods.content.content import content_list as content_list_fun
from mod.mods.content.urlapi import URL as _urlapi

AtRuntimeForTheFirstTime


def main(api):
    api['GetAllContentTemplates'] = GetAllContentTemplatesAPI
    api['NewContent'] = NewContent
    api['change'] = change
    api['ZUOzhEreadApi'] = ZUOzhEreadApi
    api['urlapi'] = url_api
    api['ContentList'] = content_list
    return api


def content_list(get_or_post, enable_session, rep, **para):
    del enable_session
    del para
    paging = int(get_or_post('paging', 8))
    number_pages = int(get_or_post('number_pages', 1)) - 1
    content_presentation = bool(get_or_post('content_presentation', False))
    c_list = content_list_fun()
    a_list = []
    try:
        return rep(json.dumps(c_list[paging * number_pages:paging * (number_pages + 1)]))
    except:
        return rep(json.dumps(c_list[paging * number_pages:len(c_list)]))


def url_api(get_or_post, EnableSession, rep, **para):
    url = get_or_post('url')
    if (url == None):
        rep('OK')
    else:
        obj = _urlapi()
        return rep(obj.LoadContent(url))


def GetAllContentTemplatesAPI(get_or_post, EnableSession, rep, **para):
    from mod.mods.content.ORSCFS import ContentTemplate as ContentTemplates
    return rep(json.dumps(ContentTemplates))


def NewContent(get_or_post, EnableSession, rep, **para):
    s = EnableSession()
    import sdk.other as other
    LimitsOfAuthority = other.CoreConfiguration(session=s)

    def a():
        Title, alias, content = get_or_post('Title'), get_or_post('alias'), get_or_post('content')
        if (content == None): return rep('参数不完整')
        con = content_obj(session=s, Title=Title, alias=alias, content=content)
        try:
            con.new()
        except:
            return rep('内容不存在')
        con.SubmitToDatabase()  # 提交
        return rep('OK')

    if (LimitsOfAuthority.administrators):
        del LimitsOfAuthority
        return a()
    elif (LimitsOfAuthority.ContentEditingRights):
        del LimitsOfAuthority
        return a()
    else:
        del LimitsOfAuthority
        return rep('No use authority')


def change(get_or_post, EnableSession, rep, **para):
    s = EnableSession()
    import sdk.other as other
    LimitsOfAuthority = other.CoreConfiguration(session=s)

    def a():
        Title, alias, content = get_or_post('Title'), get_or_post('alias'), get_or_post('content')
        if (content == None): return rep('参数不完整')
        con = content_obj(session=s, Title=Title, alias=alias, content=content)
        try:
            con.change()
        except:
            return rep('内容不存在')
        con.SubmitToDatabase()  # 提交
        return rep('OK')

    if (LimitsOfAuthority.administrators):
        del LimitsOfAuthority
        return a()
    elif (LimitsOfAuthority.ContentEditingRights):
        del LimitsOfAuthority
        return a()
    else:
        del LimitsOfAuthority
        return rep('No use authority')


def ZUOzhEreadApi(get_or_post, EnableSession, rep, **para):
    s = EnableSession()
    alias = get_or_post('alias')
    con = content_obj(session=s, alias=alias)
    con.Pulling()
    return rep(con.read())
