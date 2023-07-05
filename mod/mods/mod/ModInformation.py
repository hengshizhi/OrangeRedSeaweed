# mod information
import json
import os
import importlib
import PathInfo as PathInfo


def modlist() -> dict:
    '''mod information list'''
    return PathInfo.Dict('./mod/mods', './')


def information(ModName) -> dict:
    '''Obtain information about the module'''
    # path = f'{os.path.abspath(os.path.dirname(os.path.dirname(__file__)))}{ModName}'
    b = importlib.import_module('..{ModName}.Information'.format(ModName=ModName), __package__)
    return b.information


def logo(ModName) -> bytes:
    b = importlib.import_module('..{ModName}.Information'.format(ModName=ModName), __package__)
    return b.logo
