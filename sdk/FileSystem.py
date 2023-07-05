# from fileApi.file import Main as file_Main
# from fileApi.route import Main as route_Main
from fileApi import PathInfo as PathInfo_SDKs

import fileApi.file
import fileApi.route

PathInfo_SDK = PathInfo_SDKs()


class SDK(fileApi.file.Main, fileApi.route.main):
    pass
