# Mod mechanism entry
import importlib
from sanic.response import text
import time,sys,os

def main(get_or_post,EnableSession,rep,**para):
    ModName = get_or_post('ModName')
    ApiName = get_or_post('ApiName')
    if (ModName == None or ApiName == None):
        return rep(text('Missing "ModName" or "ApiName" parameters',status=400))
    else:
        b = importlib.import_module('.mods.{ModName}.main'.format(ModName=ModName), __package__)
        return b.main(api = {})[ApiName](get_or_post,EnableSession,rep,**para)
