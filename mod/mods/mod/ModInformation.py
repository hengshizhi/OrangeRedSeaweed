# mod information
import json
import PathInfo as PathInfo
import os
import importlib
def modlist() -> dict:
    '''mod information list'''
    return PathInfo.Dict('./mod/mods','./')

def information(ModName) -> dict:
    '''Obtain information about the module'''
    # path = f'{os.path.abspath(os.path.dirname(os.path.dirname(__file__)))}{ModName}'
    b = importlib.import_module('..{ModName}.Information'.format(ModName=ModName), __package__)
    return b.information