# Mod mechanism entry
import importlib
from sanic.response import text
import PathInfo as PathInfo

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
        return b.main(api = {})[ApiName](get_or_post,EnableSession,rep,**para)

def AtRuntimeForTheFirstTime():
    '''
    This function is called every time the program runs
    used to load the code for all mod program runtime
    '''
    for k,v in modlists().items():
        try:
            ImportMod(k).AtRuntimeForTheFirstTime() # Functions that will be executed every time the program runs mod
        except:
            pass # No self starting function

AtRuntimeForTheFirstTime()