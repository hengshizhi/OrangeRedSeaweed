# Mod mechanism entry
# /api/mod?ModName=ModName&ApiName=ApiName
import importlib
from sanic.response import text
import fileApi.PathInfo as PathInfo

def modlists() -> dict:
    '''mod information list'''
    return PathInfo.Dict('./mod/mods','./')
def ImportMod(ModName):
    b = importlib.import_module('.mods.{ModName}.main'.format(ModName=ModName), __package__)
    return b
def main(get_or_post,EnableSession,rep,**para):
    ''' 
    Main function when mod is actively called 
    Applied to HTTP API
    '''
    ModName = get_or_post('ModName')
    ApiName = get_or_post('ApiName')
    if (ModName == None or ApiName == None):
        return rep(text('Missing "ModName" or "ApiName" parameters',status=400))
    else:
        b = ImportMod(ModName)
        # try:
        return b.main(api = {})[ApiName](get_or_post,EnableSession,rep,**para)
        # except TypeError as e:
        #     if (str(e) == ''''NoneType' object is not subscriptable'''):
        #         return rep(text('mod api 为空',500) )
        # except KeyError as e:
        #     return rep(text('API 不存在',500) )
def AtRuntimeForTheFirstTime():
    '''
    This function is called every time the program runs
    used to load the code for all mod program runtime
    '''
    for k,v in modlists().items():
        try:
            ImportMod(k).AtRuntimeForTheFirstTime() # Functions that will be executed every time the program runs mod
        except AttributeError as e:
            pass # No self starting function
            print( f'mod "{k}" 加载成功,但是不存在初始加载函数,报错:'+str(e) )
        else:
            print(f'mod "{k}" 加载成功')
AtRuntimeForTheFirstTime()