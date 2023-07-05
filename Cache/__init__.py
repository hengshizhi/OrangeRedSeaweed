import Cache.Memory 
import Cache.UnderlyingMethods as UM
class CacheObj():
    def __init__(self,name:str,read:object,SubmitTo:object,renew:object) -> None:
        '''
        name : Cache Name
        read : read(name) -> contant
        SubmitTo : def SubmitTo(name,contant) -> None
        '''
        self.name = name
        self.renew = read
        self.SubmitToY = SubmitTo
        self.contant = read(name)
    def Pulling(self) -> str:
        self.contant = self.read(self.name)
        return self.contant
    def SubmitTo(self) -> str:
        return self.SubmitToY (self.name,self.contant)
class Cache():
    def __init__(self,mode:object = UM.Memory) -> None:
        '''Cache functionality for plugin developers,
        The purpose of design is to exchange space for time
        mode :The class in Cache.UnderlyingMethods has a file_ Cache and Memory, default to Memory
        '''
        self.mode = mode
    def GetCache(self,name):
        '''Get a cached object'''
    def NewCache(self,name,function):
        '''
        You can create a new cache and return a class for calling the cache
        Parameters:
        name: Cache name
        function: Get the function used by the cache
        '''
