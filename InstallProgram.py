print('''注意安装前需要填写好两项配置:
数据库连接配置，路径:./operation/db/config.py
其他配置，路径:./operation/config.py
''')
import sys
import os

sys.path.append(os.getcwd() + '/operation/')
try:
    import operation.user as user
except:
    print('请检查数据库配置是否正确')
import time
import sdk.other as other
import operation.session as session

# OTHERDATA = other.Main('CoreConfiguration',True,1686191036)
# OTHERDATA.data['administrators'] = 1
# OTHERDATA.SubmitToDatabase()

while 1:
    a = input('输入：安装【一】，登录【二】')
    if (a == '一'):
        try:
            print(user.registered_record(id=2, nickname='User Data User', postbox='UserDataUser@email.com'))
        except:
            print('已经安装过')
        id = time.time()
        id = int(id + 0.5)  # 四舍五入
        user.registered_record(id=id, postbox=input('你的邮箱(必填,否则可能导致系统错乱):'), nickname=input('你的昵称:'))
        OTHERDATA = other.Main('CoreConfiguration', True, id)
        OTHERDATA.data['administrators'] = True
        OTHERDATA.SubmitToDatabase()
        print(f'注册完成，id:{id}')
        print('成功设置管理员')

    elif (a == '二'):
        sessionid = input('sessionid(new?):')
        id = user.get_user_data(postbox=input('你的邮箱').replace(' ', ''))['id']
        if (sessionid == 'new' or sessionid == '' or sessionid == None):
            s = session.session()
            s.create()
        else:
            s = session.session(session_key=sessionid)
            s.getDB()
        s.data['login_status_id'] = id
        s.refresh()
        print(f'登录成功，SessionId：{s.key}')
    elif (a == '三'):
        OTHERDATA = other.Main('CoreConfiguration', True, input('你的id'))
        OTHERDATA.Pulling()
        print(OTHERDATA.data)
