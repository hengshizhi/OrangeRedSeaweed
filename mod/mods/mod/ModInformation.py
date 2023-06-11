# mod information
import json
import PathInfo as PathInfo
def modlist():
    '''mod information list'''
    return json.dumps(PathInfo.Dict('./mod/mods','./'))