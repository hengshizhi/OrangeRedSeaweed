# mod information
import json
import PathInfo as PathInfo
def modlist() -> dict:
    '''mod information list'''
    return PathInfo.Dict('./mod/mods','./')