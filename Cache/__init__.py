import Cache.Memory as Memory
import Cache.UnderlyingMethods as UM


class CacheObj():
    def __init__(self, name: str,
                  read: object = lambda name:str
                 , SubmitTo: object = lambda name,contant:None, 
                 renew: object = lambda :str,
                 delete: object = lambda name:None) -> None:
        '''
        name : Cache Name
        read : def read(name) -> contant || Extract data from cache
        >>>
        SubmitTo : def SubmitTo(name,contant) -> None || Submit data to cache
        >>>
        renew : renew() -> contant || Used to obtain data from a data source
        >>>
        delete : delete(name) -> None || Used to delete cache
        >>>
        '''
        self.name = name
        self.read = read
        self.SubmitToY = SubmitTo
        self.renew1 = renew
        self.contant = renew()
        self.SubmitTo()
        self._del = delete
    def Pulling(self):
        self.contant = self.read(self.name)
        return self.contant

    def SubmitTo(self) -> str:
        return self.SubmitToY(self.name, self.contant)

    def renew(self):
        self.contant = self.renew1()
        self.SubmitTo()
        return self.renew1()

    def delete(self):
        '''删除本缓存'''
        self._del(self.name)
class Cache():
    def __init__(self, mode: object = UM.Memory) -> None:
        '''Cache functionality for plugin developers,
        The purpose of design is to exchange space for time
        mode :The class in Cache.UnderlyingMethods has a file_ Cache and Memory, default to Memory
        '''
        self.mode = mode()
    def GetCache(self, name: str):
        '''Get a cached object'''
        return Memory.Caches[name]

    def NewCache(self, name: str, function: object):
        '''
        You can create a new cache and return a class for calling the cache
        Parameters:
        name: Cache name
        function: Get the function used by the cache
        '''

        def read(name):
            return self.mode.read(name)

        def SubmitTo(name, contant):
            return self.mode.New(name, contant)

        Memory.Caches[name] = CacheObj(name, read, SubmitTo, function, self.mode.delete)
        return Memory.Caches[name]
