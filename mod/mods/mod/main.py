# mod插件
import json

import sdk.other as other
from sanic.response import HTTPResponse

from .ModInformation import information
from .ModInformation import logo as Ilogo
from .ModInformation import modlist
from .ModJs import modjs as modjsObj


def AtRuntimeForTheFirstTime():
    ''' Functions that will be executed every time the program runs mod '''
    pass


def main(api):
    return {'Modlist': apiModlist,
            'modjs': apiModjs,
            'logo': logo,
            'GetInformation': GetInformation
            }


def apiModlist(get_or_post, EnableSession, rep, **para):
    s = EnableSession()
    try:
        OT = other.Main('CoreConfiguration', True, s.data['login_status_id'])
    except:
        return rep('You are not logged in')
    if (OT.AdministratorVerification(s)):  # Administrator verification
        return rep(json.dumps(modlist()))
    else:
        return rep('You not is administrators')


def apiModjs(get_or_post, EnableSession, rep, **para):
    return rep(modjs())


def apiDelmod(get_or_post, EnableSession, rep, **para):
    pass


def apiAddmod(get_or_post, EnableSession, rep, **para):
    pass


def apiDisableMod(get_or_post, EnableSession, rep, **para):
    pass


def BackgroundManagement(get_or_post, EnableSession, rep, **para):
    '''后台管理'''


def logo(get_or_post, EnableSession, rep, **para):
    '''mod logo'''
    modName = get_or_post('LogoModName')
    logos = Ilogo(modName)
    return rep(HTTPResponse(logos, content_type='image/jpeg'))


def GetInformation(get_or_post, EnableSession, rep, **para):
    modName = get_or_post('LogoModName')
    inf = information(modName)
    return rep(json.dumps(inf))


def modjs() -> str:
    ret = ''
    modlsit = modlist()
    for k, v in modlsit.items():
        Modjs = modjsObj(k)
        ret += Modjs.output()
    return ret


def delmod():
    pass


def addmod():
    pass


def DisableMod():
    '''禁用原理:改mod路径名'''
