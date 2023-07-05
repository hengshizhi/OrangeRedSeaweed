# The underlying method of cache retrieval
import fileApi.route as route
import fileApi.file as file
import os
class file_Cache():
    def __init__(self,path = './Cache/data') -> None:
        route.mkdir(path)
        self.path = path
    def openw(self,name,con):
        '''写入'''
        with open(os.path.normpath(f'{self.path}/{name}')) as f:f.write(con)
    def openr(self,name):
        '''查看'''
        with open(os.path.normpath(f'{self.path}/{name}'),encoding='utf-8') as f:return f.read()
    def New(self,name,con):
        '''
        name :缓存名字
        con :缓存内容
        '''
        