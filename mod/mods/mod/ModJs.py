# Modjs is the output function of the JavaScript code used for mod loading
# Call "modjs.output()" to return the JavaScript code of all mod, and use the front-end to include loading
# Modjs will call modjs() in the "frontendModjs.py" under each mod
# Add the returned JavaScript code to the return value of "modjs.output()"

from .ModInformation import modlist
import importlib

class modjs():
    def __init__(self,ModName) -> None:
        '''
        Modjs is the output function of the JavaScript code used for mod loading
        Call "modjs.output()" to return the JavaScript code of all mod, and use the front-end to include loading
        Modjs will call modjs() in the "frontendModjs.py" under each mod
        Add the returned JavaScript code to the return value of "modjs.output()"
        parameter :
            ModName : mod's name
        '''
        # Load frontendModjs
        self.ModName = ModName
        try:
            self.b = importlib.import_module('..{ModName}.frontendModjs'.format(ModName=ModName), __package__)
        except:
            pass
    def output(self) -> str:
        '''Output the front-end JavaScript code corresponding to mod'''
        try:
            return f'{self.b.modjs()}\n'
        except:
            return f'var {self.ModName}=null;\n'
