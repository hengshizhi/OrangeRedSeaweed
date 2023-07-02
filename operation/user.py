#用户相关
import time as time
from sanic.response import text,json,redirect
import random
import string
import random
import json
from sanic.response import text
# try:
import operationconfig as configs
import md5 as md5
import db.mysql as db
from mail import mail as mails
# except:
#     # import md5 as md5
#     import db.mysql as db
#     from mail import mail as mails
#     import config as configs
get_session = db.get_session
User = db.table.User
mail = mails()
config = configs.information()
def registered_record(id=time.time(),#设置主键
    name=time.time(),#用户名
    Key=md5.get_md5(''.join(random.sample(string.ascii_letters + string.digits, 20))),#密码
    Registration_time=time.time(),#注册时间
    postbox=False,#邮箱
    nickname='空的',#昵称
    HeadPortrait=''#头像(url)
):
    '''
    添加注册用户记录
    ->
    '''
    if(bool(id) and 
       bool(postbox)
    ):    
        with get_session() as s:
            user = User()
            user.id = id
            user.name = name
            user.Key = 1
            user.Registration_time = Registration_time
            user.postbox = postbox
            user.nickname = nickname
            user.created_at = time.time()
            # user.HeadPortrait = HeadPortrait
            # user.LastLogin = 0
            s.add(user)
            s.commit()
            return id
    else:
        return False
def login_Password_authentication(id=False,name=False,postbox=False,Key=False):
    '''
    登录密码验证,支持：
    id登录:id
    用户名登录:name
    邮箱登录:postbox
    密码:Key
    '''
    with get_session() as s:
        if(id and s.query(User).filter(User.id == id,User.Key == Key).first() != []):
            return True
        elif(name and s.query(User).filter(User.name == name,User.Key == Key).first() != []):
            return True
        elif(postbox and s.query(User).filter(User.postbox == postbox,User.Key == Key).first() != []):
            return True
        else:
            return False
def get_user_data(id=False,name=False,postbox=False):
    '''
    获得用户数据：
    可以传入id,name,postbox
    返回用户数据,格式可以参照user表
    '''
    with get_session() as s:
        try:id_data = s.query(User).filter(User.id == id,User.deleted_at == None).first()
        except:id_data = None
        try:name_data = s.query(User).filter(User.name == name,User.deleted_at == None).first()
        except:name_data = None
        try:postbox_data = s.query(User).filter(User.postbox == postbox,User.deleted_at == None).first()
        except:postbox_data = None
        if(id and id_data != None):data = id_data
        elif(name and name_data != None):data = name_data
        elif(postbox and postbox_data != None):data = postbox_data
        else:return None
        ret = data.single_to_dict()
        return ret #将结果转换成dict

def Change_user_data(id=False,name=False,postbox=False,data:dict = {}):
    '''
    更改用户数据
    data: 要更改的数据
    '''
    with get_session() as s:
        for k,v in data.items():
            if (not (k == 'id' or k == 'postbox' or k == 'Registration_time' or k == 'name')):
                if(id):
                    s.query(User).filter(User.id == id).update({k:v})
                elif(name):
                    s.query(User).filter(User.name == name).update({k:v})
                elif(postbox):
                    s.query(User).filter(User.postbox == postbox).update({k:v})
                else:
                    return False
    return True
def GET_other_user_data_interior(user_id=False,name=False,postbox=False,id:str=''):
    '''获得用户其他数据(DATA字段)
    id :其他数据中的键值
    '''
    # data = json.loads(get_user_data(id=user_id,name=name,postbox=postbox)['DATA'])
    # return data[id]
    try:
        data = get_user_data(id=user_id,name=name,postbox=postbox)['DATA']
        data =  eval(data)
    except:
        data = {}
        data[id] = None
        Change_user_data(id =user_id,data={'DATA':str(data)}) #更新用户数据
        return data[id]
    try:return data[id]
    except: #假如没有创建键
        data[id] = None
        Change_user_data(id =user_id,data={'DATA':str(data)}) #更新用户数据
    return data[id]
def Change_other_user_data_interior(user_id=False,name=False,postbox=False,id:str='',v:str=''):
    '''
    更改用户其他数据(DATA字段)
    parameter :
        v: 要更新的数据(json)
    '''
    try:
        data = eval(get_user_data(id=user_id,name=name,postbox=postbox)['DATA'])
    except: # 没有使用过其他用户数据的情况
        data = {}
        data[id] = None
        data[id] = v # 保存键
        Change_user_data(id =user_id,data={'DATA':str(data)}) #更新用户数据
        return str(data[id])
    try:
        data[id] = v # 保存键
        Change_user_data(id =user_id,data={'DATA':str(data)}) #更新用户数据
    except: #假如没有键值则创造键值
        data[id] = None
        data[id] = v # 保存键
        Change_user_data(id =user_id,data={'DATA':str(data)}) #更新用户数据
    return str(data[id])
def Traverse_other_data_with_the_same_key_value(id:str=''):
    '''
    遍历其他数据的同一键值
    return :dict({<user-id>:<其他数据>,...})
    示例：当id='CoreConfiguration'时返回{'1686193681': {'administrators': True}}
    '''
    rep = {}
    with get_session() as s:
        for i in s.query(User).all():
            i = i.dobule_to_dict()
            if (i == None): continue
            else:
                try: data_is_idis = eval(i['DATA'])[id]
                except: continue
                rep[i['id']] = data_is_idis
    return rep
def QQ_online_status(QQID):
    import requests
    req = requests.get('http://www.webxml.com.cn/webservices/qqOnlineWebService.asmx/qqCheckOnline?qqCode={QQID}'.format(QQID=QQID))
    req = req.text
    # .replace('<string xmlns="http://WebXml.com.cn/">','').replace('</string>','').replace('<?xml version="1.0" encoding="utf-8"?>','').replace('\n','')
    if('Y' in req):
        return True
    elif('N' in req):
        return False
    elif('E' in req):
        return None
    raise Exception('请求webservicesAPI错误')

class api():
    '''
    session['login_status_id'] :用户登录状态,登录的id
    '''
    config = configs.Email_login() # 获取邮件配置 

    def apiDict(self):
        return  {
        'login_SendEmainVerification_API' : self.login_SendEmainVerification_API, # 登录
        'login_Email_Verifier_API': self.login_Email_Verifier_API, #验证验证码
        'registered': self.registered, # 注册
        'get_user_data':self.get_user_data, # 获取用户信息
        'GetorChange_other_user_data':self.GetorChange_other_user_data, # 修改或查看用户数据
        'login_status':self.login_status, #获取登录状态
        'HeadSculpture':self.HeadSculpture, #获取头像地址
        'GetNickname' : self.GetNickname, #获得昵称
        'Change_user_data':self.Change_user_data, # 更改用户数据
        }
    def Change_user_data(self,get_or_post,EnableSession,rep,**para): # 更改用户数据
        s = EnableSession() # 开启Session
        try:user_id = s.data['login_status_id'] # 获得登录状态
        except:return para['RepisOldVersion'](s,'Not logged in')
        try:
            data =json.loads(get_or_post('data'))
        except:return para['RepisOldVersion'](s,'Require JSON')
        if (Change_user_data(id=user_id,data=data)):
            return para['RepisOldVersion'](s,'OK')
        else:
            return para['RepisOldVersion'](s,'internal error')
    def login_status(self,get_or_post,s,rep,**para):
        '''获取登录状态'''
        s = s()
        if(s.get('login_status_id')):
            return para['RepisOldVersion'](s,json.dumps({'state':str(True),'id':s.get('login_status_id')}))
        else:
            return para['RepisOldVersion'](s,'None')

    def GetorChange_other_user_data(self,get_or_post,EnableSession,rep,**para):
        '''
        得到其他的用户数据:
        方便lci其他平台得到保存在lci-org-user的数据
        需要id:key
        验证key正确之后
        获取对应id:data
        例子:
        > id:key
        < user_data
        '''
        s = EnableSession()
        try:user_id = s.data['login_status_id'] # 获得登录状态
        except:return para['RepisOldVersion'](s,'Not logged in')

        # 获得参数
        key = get_or_post('key',False)
        id = get_or_post('id',False)
        v = get_or_post('v',False)
        if(not key):return para['RepisOldVersion'](s,'Incomplete parameters (key)')
        elif(not id):return para['RepisOldVersion'](s,'Incomplete parameters (id)')
        else:
            try:
                OUDGK = configs.OtherUserDataGetsKey[id]
            except:
                return para['RepisOldVersion'](s,'Incorrect(id)') #判断id是否存在
            if(OUDGK == key):
                if(v): # 是否有数据,如果有数据就更改数据,没有就查看数据
                    return para['RepisOldVersion'](s,Change_other_user_data_interior(user_id=user_id,id=id,v=v)) # 更改数据
                else:
                    return para['RepisOldVersion'](s,GET_other_user_data_interior(user_id=user_id,id=id)) #获得数据
            elif(OUDGK != key):
                return para['RepisOldVersion'](s,'Incorrect(key)') #key is not
            else:
                return para['RepisOldVersion'](s,'Strange reasons lead to failure')
    def registered(self,get_or_post,s,rep,**para):
        '''注册'''
        # 接收参数:
        s = s()
        name = get_or_post('name',time.time()) #用户名
        Key = get_or_post('Key'.format(),True) #密码
        postbox = get_or_post('postbox',False) #邮箱
        nickname = get_or_post('nickname',True) #昵称

        if(get_user_data(postbox=postbox) != None): #获得用户数据,如果不是None证明已经存在用户
            return {'async':False,
                    'data':text('User already exists'),
                    'cookie':{'Session_key':''},
                    'session_odj':s
                    }
                    
        id = registered_record(name=name,
                          Key=Key,
                          postbox=postbox,
                          nickname=nickname
                          ) #注册,提交到数据库,返回注册之后的id

        if(id):
            return para['RepisOldVersion'](s,'OK,ID->'+str(id))
        else:
            return para['RepisOldVersion'](s,'Incomplete parameters')

    def login_SendEmainVerification_API(self,get_or_post,s,rep,**para): #发送验证码并且储存验证码的API
        '''
        登录验证
        '''
        s = s()
        if(s.get('login_status_id')):return {'async':False,'data':text('Is logged in'),'cookie':{'Session_key':''},'session_odj':s}
        def login_Verification(self,id=False,name=False,postbox=False): #获取验证码(登录)并且发送
            data = get_user_data(id,name,postbox)
            Verification = random.randint(1, 5000000) #获取验证码
            if(data != None):
                try:
                    mail.send(self.config.TEMPlate
                            .format(Verification=Verification,
                                    nickname = data['nickname'],
                                    name = data['name'],
                                    websiteName = config.name,
                                    SessionKey=s.key
                                    ),
                            self.config.Theme
                            .format(Verification=random.randint(1, 5000000),
                                    nickname = data['nickname'],
                                    name = data['name'],
                                    websiteName = config.name,
                                    SessionKey=s.key
                                    ),
                            {'nickname':data['name'],'address':data['postbox']})
                except:
                    return False #邮件发送失败
            else:
                return None #不存在此用户
            return [Verification,data['id']] #成功,返回验证码

        #接收参数
        user_name = get_or_post('user_name',get_or_post('name',False))
        user_id = get_or_post('user_id',get_or_post('id',False))
        user_postbox = get_or_post('user_postbox',get_or_post('postbox',False))

        if(not user_name and not user_postbox and not user_id):
            return para['RepisOldVersion'](s,'Parameter is not complete')

        Verification = login_Verification(self,user_id,user_name,user_postbox) #获取并发送验证码

        s.Set('Verification',Verification[0])
        s.Set('user_id',Verification[1])
        return para['RepisOldVersion'](s,'OK,ID->'+str(Verification[1]))
    def login_Email_Verifier_API(self,get_or_post,s,rep,**para):
        '''
        验证验证码是否正确,并登录
        '''
        s = s()
        # HTTP参数：Verification（验证码）,用于登录验证
        GetVerification = get_or_post('Verification') #得到的验证码
        # return rep(s,str(s.get('Verification')))
        if(str(s.get('Verification')) == str(GetVerification)):
            Change_user_data(id = s.data['user_id'],data={'LastLogin':time.time()}) #更改用户数据
            s.Set('login_status_id',s.data['user_id']) #设置登录状态
            s.delete(['user_id','Verification']) #删除待验证用户id,删除验证码
            # print(s.data)
            return {'async':False,
            'data':text('OK,ID->'+str(s.data['login_status_id'])),
            'cookie':{'Session_key':''},
            'session_odj':s
            }
        else:
            return {'async':False,
            'data':text('Verification code error'),
            'cookie':{'Session_key':''},
            'session_odj':s
            }
    def get_user_data(self,get_or_post,s,rep,**para):
        s = s()
        try:
            ret = get_user_data(id=s.data['login_status_id'])
            del ret['DATA']
            del ret['deleted_at']
            del ret['updated_at']
            return para['RepisOldVersion'](s,str(json.dumps(ret)))
        except:
            return para['RepisOldVersion'](s,'You may not be logged in')
    def HeadSculpture(self,get_or_post,s,rep,**para): #获取头像地址
        s = s()
        id = get_or_post('id',False)
        name = get_or_post('name',False)
        postbox = get_or_post('postbox',False)
        if(id or name or postbox):pass
        elif(s.get('login_status_id') != None):id = s.get('login_status_id')
        else:return para['RepisOldVersion'](s,'Parameter is not complete')
        data = get_user_data(id,name,postbox)
        hash = md5.get_md5(data['postbox'])
        return {'async':False,
        'data':redirect("https://cravatar.cn/avatar/{hash}".format(hash=hash)),
        'cookie':{'Session_key':''},
        'session_odj':s
        }
    def GetNickname(self,get_or_post,s,rep,**para):
        s = s()
        id = get_or_post('id',False)
        name = get_or_post('name',False)
        postbox = get_or_post('postbox',False)
        if(id or name or postbox):pass
        elif(s.get('login_status_id') != None):id = s.get('login_status_id')
        else:return para['RepisOldVersion'](s,'Parameter is not complete')
        data = get_user_data(id,name,postbox)
        return para['RepisOldVersion'](s,data['nickname'])