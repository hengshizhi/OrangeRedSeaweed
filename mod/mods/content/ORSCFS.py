# 提供内容格式转换
import json

ContentTemplate = {}

class content:
    def __init__(self, ORSCFS_STR):
        self.content = ORSCFS_STR # ORSCFS 内容 字符串
    def html(self):
        pass

def content_generation(title, content, author , ReleaseDate):
    return json.dumps({
        'title': title,
        'content': content,
        'author': author,
        'ReleaseDate': ReleaseDate
    })


