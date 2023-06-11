# mod插件
import json
import sdk.other as other
from .ModInformation import modlist
def main(api):
    return {'Modlist':apiModlist}
def apiModlist(get_or_post,EnableSession,rep,**para):
    s = EnableSession()
    OT = other.Main('CoreConfiguration',True,s.data['login_status_id'])
    if (OT.AdministratorVerification(s)): # Administrator verification
        return modlist()
    else:
        return rep('You not is administrators')
def apiModjs(get_or_post,EnableSession,rep,**para):
    pass
def apiDelmod(get_or_post,EnableSession,rep,**para):
    pass
def apiAddmod(get_or_post,EnableSession,rep,**para):
    pass
def apiDisableMod(get_or_post,EnableSession,rep,**para):
    pass
def BackgroundManagement(get_or_post,EnableSession,rep,**para):
    '''后台管理'''


def modjs() -> str:
    pass
def delmod():
    pass
def addmod():
    pass
def DisableMod():
    '''禁用原理:改mod路径名'''
