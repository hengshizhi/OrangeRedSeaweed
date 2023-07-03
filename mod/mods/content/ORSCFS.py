# 提供内容格式转换
import json

ContentTemplate = {}

class content:
    def __init__(self, ORSCFS_STR):
        self.content = json.loads(ORSCFS_STR) # ORSCFS 内容 字符串
    def html(self):
        ret = ''
        for i in self.content:
            ret += self. jiazaidangemoban(i)
        return ret
    def jiazaidangemoban(self,ot:dict):
        '''加载单个模板'''
        name = ot['name'].split(':')
        mobanneirong = ContentTemplate[name[0]][name[1]] # 模板内容
        # ret = 
        ret = mobanneirong['main']
        for k,v in ot.items():
            for k2,v2 in mobanneirong['format'].items():
                for k3,v3 in ContentTemplate[name[0]]['GlobalFormat'].items():
                    k3if = k == k3
                    if ((k == k2 or k3if)  and k != 'name'):
                        if (v == None):
                            if (k3if):
                                ret = self.format(k3,k3['Default'],ret)
                            else:
                                ret = self.format(k2,v2['Default'],ret)
                            break
                        ret = self.format(k,v,ret)
                        break
        return ret
    def format(self,k,v,str1:str):
        return str1.replace('<~'+k+'~>',str(v))
def content_generation(title, content, author , ReleaseDate):
    return json.dumps({
        'title': title,
        'content': content,
        'author': author,
        'ReleaseDate': ReleaseDate
    })