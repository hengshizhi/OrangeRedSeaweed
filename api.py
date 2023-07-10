# api回调类

from sanic.response import text, empty

from mod.mod import main as modmian
from operation.session import session
from operation.user import api as user
from sdk.other import CoreConfiguration as ccf
user = user()

def restart_program_func():
    import sys, os
    python = sys.executable
    os.execl(python, python, *sys.argv)

def restart_program(get_or_post, enableSession, rep, **para):
    '''重启程序'''
    qunaxian = ccf(session=enableSession())
    if (qunaxian.administrators):
        restart_program_func()
    else:
        return rep('未登录')

def get_session_key(get_or_post, EnableSession, rep, **para):
    s = EnableSession()
    return rep(s.key, s)


# def helloWorld(get_or_post, EnableSession, rep, **para):
#     '''
#     parameter :
#         get_or_post :获取get或者post参数
#         EnableSession :开启Session使用
#         rep :生成返回对象
#         **para : 注:本字典可能会随着需求变化而变化
#             {'request':<sanic's "request" object>}
#     '''
#     s = EnableSession()  # 开启Session
#     s.data = {'bbb': 'aaaa'}
#     s.refresh()
#     s.getDB()
#     return {'async': False,
#             'data': text(str(s.data)),
#             'cookie': {'Session_key': ''}, 'session_odj': s
#             }

# apiDict = {'helloWorld': helloWorld}
api_dict = {'Get_session_key': get_session_key,
            'mod': modmian,
            'restart_program':restart_program}
api_dict.update(user.apiDict())  # 添加lci-user


def main(request, name):
    try:  # api是否存在
        if (type(api_dict[name]) == None):
            return {'data': empty(status=404)}
    except:
        return {'data': empty(status=404)}

    def RepisOldVersion(session_odj, data, cookie={}): # 老版本 rep()
        return {'async': False,
                'data': text(data),
                'cookie': cookie,
                'session_odj': session_odj
                }

    def rep(data, session_odj=None, cookie={}, ):
        if (type(data) == str):
            return {'async': False,
                    'data': text(data),
                    'cookie': cookie,
                    'session_odj': session_odj
                    }
        else:
            return {'async': False,
                    'data': data,
                    'cookie': cookie,
                    'session_odj': session_odj
                    }

    def get_or_post(key, output=None, request=request):  # 如果没有GET参数就用post
        '''
        key:需要接收参数的键值
        output:返回格式,如果没有此参数就返回它,默认None
        '''
        if (request.args.get(key) != None):
            return request.args.get(key)
        elif (request.form.get(key) != None):
            return request.form.get(key)
        return output

    def EnableSession():
        '''启用会话
        parameter :None
        return :session_odj
        '''
        session_key = get_or_post('SessionKey')
        if (session_key == None):
            session_key = get_or_post('SessionID')
        if (session_key == None): session_key = request.cookies.get("Session_key")
        session_odj = session(session_key)  # 实例化session
        if (session_key == None or session_key == ''): session_odj.create()  # 没有Session时创建Session_key
        try:
            session_odj.getDB()  # 将数据库的session同步到内存,这一句话错误代表session失效
        except:
            session_odj.key = request.cookies.get("Session_key")
            try:
                session_odj.getDB()  # 如果cookies里面的session也失效,就创建
            except:
                session_odj.create()
                session_odj.getDB()
        print('NEWsession_key:', session_odj.key)
        return session_odj

    ret = api_dict[name](get_or_post, EnableSession, rep, request=request, RepisOldVersion=RepisOldVersion)
    if (ret['session_odj'] != None):
        try:
            session_odj = ret['session_odj']  # 覆写session_odj为更改过的session_odj
            session_odj.refresh()  # 提交内存的session
        except:
            print('提交失败')
        try:
            ret['cookie']['Session_key'] = session_odj.key  # 更新cookie的session_key
        except:
            pass
    return ret
