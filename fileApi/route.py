#路径操作类
import os
import shutil

class main:
    def mkdir(self,path): #创建目录
        folder = os.path.exists(path)
        if not folder:                   #判断是否存在文件夹如果不存在则创建为文件夹
            os.makedirs(path)            #makedirs 创建文件时如果路径不存在会创建这个路径
            return True
        else:
            return False
    def rename(self,old,new): #重命名
        '''重命名文件或者目录
        参数：
            old:重命名前的目录或文件
            new:重命名后的目录或文件
        '''
        try:
            os.rename(old,new)
            return True
        except:
            return False #源文件或者目录找不到
    def CopyCatalog(self,old,new):
        '''复制目录
        参数：
            old:复制前的路径
            new:复制后的路径
        '''# shutil.copyfile
        if(os.path.isdir(old) and not os.path.isdir(new)): #需要复制前的文件存在,复制的目标路径不存在
            shutil.copytree(old,new) #复制成功
            return True
        else:
            return False