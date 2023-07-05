# from fileApi.file import Main as file_Main
# from fileApi.route import Main as route_Main
import fileApi.route
from fileApi import PathInfo as PathInfo_SDKs

PathInfo_SDK = PathInfo_SDKs()


class SDK(fileApi.file.Main, fileApi.route.main):
    pass
