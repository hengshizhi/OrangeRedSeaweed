# The underlying method of cache retrieval
import Cache.Memory as Memory1
import fileApi.file as file
import fileApi.route as route


class file_Cache():
    def __init__(self) -> None:
        '''Utilizing file storage caching (not recommended)'''
        path = './Cache/data/'
        route.mkdir(path)
        self.file = file.New(path)

    def New(self, name, con):
        self.file.openw(name, str(con))

    def read(self, name):
        return eval(self.file.openr(name))

    def delete(self,name):
        self.file.delete(name)

class Memory:
    def __init__(self) -> None:
        '''Using Memory to Store Caches'''
        pass

    def New(self, name, con): Memory1.data[name] = con

    def read(self, name): return Memory1.data[name]

    def delete(self,name): del Memory1.data[name]