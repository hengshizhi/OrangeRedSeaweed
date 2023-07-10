# This is frontendModjs.py,
# which is used to store the modjs() function that returns the module JavaScript code
from fileApi.file import New as file
def modjs() -> str:
    f = file('.\mod\mods\content')
    return f.openr('mod_js.js')
