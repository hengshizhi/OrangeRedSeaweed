import Cache.Memory 
import Cache.UnderlyingMethods as UM
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
