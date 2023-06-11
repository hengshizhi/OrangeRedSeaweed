# mod插件
import json
import sdk.other as other
from .ModInformation import modlist
from .ModJs import modjs as modjsObj
def main(api):
    return {'Modlist':apiModlist,
            'modjs':apiModjs
            }
def apiModlist(get_or_post,EnableSession,rep,**para):
    s = EnableSession()
    try:
        OT = other.Main('CoreConfiguration',True,s.data['login_status_id'])
    except:
        return rep('You are not logged in')
    if (OT.AdministratorVerification(s)): # Administrator verification
        return rep(json.dumps(modlist()))
    else:
        return rep('You not is administrators')
def apiModjs(get_or_post,EnableSession,rep,**para):
    return rep(modjs())
def apiDelmod(get_or_post,EnableSession,rep,**para):
    pass
def apiAddmod(get_or_post,EnableSession,rep,**para):
    pass
def apiDisableMod(get_or_post,EnableSession,rep,**para):
    pass
def BackgroundManagement(get_or_post,EnableSession,rep,**para):
    '''后台管理'''


def modjs() -> str:
    ret = ''
    modlsit = modlist()
    for k,v in modlsit.items():
        Modjs = modjsObj(k)
        ret += Modjs.output()
    return ret
def delmod():
    pass
def addmod():
    pass
def DisableMod():
    '''禁用原理:改mod路径名'''
