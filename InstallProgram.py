print('''注意安装前需要填写好两项配置:
数据库连接配置，路径:./operation/db/config.py
其他配置，路径:./operation/config.py
''')
import sys
import os
sys.path.append(os.getcwd()+'/operation/')
try:
    import operation.user as user
except:
    print('请检查数据库配置是否正确')
import time
import sdk.other as other
import operation.session as session

while 1:
    a = input('输入：安装【一】，登录【二】')
    if (a == '一'):
        user.registered_record(id=0,nickname='User Data User',postbox='UserDataUser@email.com')
        id = time.time()
        user.registered_record(id=id,postbox=input('你的邮箱(必填,否则可能导致系统错乱):'),nickname=input('你的昵称:'))
        print(f'注册完成，id:{id}')
        OTHERDATA = other.Main('CoreConfiguration',True,id)
        OTHERDATA.data['administrators'] = True
        OTHERDATA.SubmitToDatabase()
        print('成功设置管理员')
        
    elif(a == '二'):
        id = user.get_user_data(postbox=input('你的邮箱'.replace(' ','')))['id']
        s = session.session()
        s.create()
        s.data['login_status_id'] = id
        s.refresh()
        print(f'登录成功，SessionId：{s.key}')
        