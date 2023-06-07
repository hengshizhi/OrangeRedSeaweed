# Mod mechanism entry
from sanic.response import text
def main(get_or_post,EnableSession,rep,**para):
    ModName = get_or_post('ModName')
    ApiName = get_or_post('ApiName')
    if (ModName == None or ApiName == None):
        return rep(text('Missing "ModName" or "ApiName" parameters',status=400))