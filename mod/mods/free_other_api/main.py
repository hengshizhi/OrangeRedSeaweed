# 本模组设想一个自由的其他数据API，利用缓存保存other对象，然后利用一系列特定的
# 指令（集）来对对象进行操作，这一切都可以通过API来完成
# 需要先请求new之类函数创建对象并且获取对象的缓存位置
# 然后通过operate之类的函数利用指令集进行操作
# 有了这玩意，就可以安全+快速操作数据啦，就不用写python啦（只剩js sdk啦）
from sdk.other import Main as other
def main(api):
    api['free_other_session_new'] = free_other_session_new
    return api

def free_other_session_new(get_or_post, enable_session, rep, **para):
    obj = other(get_or_post('key'),session=enable_session())

