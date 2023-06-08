# mod插件
import PathInfo as PathInfo
import json
def main(api):
    return {'Modlist':apiModlist}
def apiModlist(get_or_post,EnableSession,rep,**para):
    return rep(json.dumps(PathInfo.Dict('./mod/mods','./')))
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

def modlist():
    pass
def modjs():
    pass
def delmod():
    pass
def addmod():
    pass
def DisableMod():
    '''禁用原理:改mod路径名'''