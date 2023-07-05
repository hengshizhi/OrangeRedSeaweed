import requests
import json


class Lci_user():
    SessionKey = None
    RURL = ''  # 服务器地址
    OtherData = ''  # 其他用户数据
    OtherID = 'LstCodeGuanli'  # 访问其他用户数据的ID
    OtherKey = 'y87238d8sny4832n8a7'  # 访问密码

    def reqapi(self, name, parameter: dict = {}):
        '''
        name :API name
        parameter :param
        '''
        kw = {'SessionKey': self.SessionKey}
        for k, v in parameter.items():
            kw[k] = None
            kw[k] = v
        return requests.post(f'{self.RURL}{name}', params=kw).text

    def __init__(self, Lci_user_url='http://lci-user.df100.ltd/api/', SessionKey=None):
        '''
        Lci_user_url :服务器地址
        SessionKey :SessionKey,可选,如果不传,就请求一个Key
        '''
        self.RURL = Lci_user_url
        self.SessionKey = SessionKey
        try:
            self.SessionKey = requests.get(self.RURL + 'Get_session_key',
                                           params={'SessionKey': self.SessionKey}).text  # 请求SessionKey
            print('Connection succeeded!')
            print('GET session key:{key}'.format(key=self.SessionKey))
        except:
            print('Failed to connect to server')

    def signup(self, name, Key, nickname, postbox=None):
        '''
        注册:
        name 用户名
        key 密码(几乎没用)
        nickname 昵称
        postbox 邮箱(必须要)
        '''
        if (postbox == None):
            raise Exception('The mailbox cannot be empty')
        return self.reqapi(name='registered', parameter={
            'name': name,
            'Key': Key,
            'postbox': postbox,
            'nickname': nickname,
        }).replace('OK, ID - > ', '')

    def logon(self, id=None, name=None, postbox=None):
        return self.reqapi(name='login_SendEmainVerification_API', parameter={
            'user_id': id,
            'user_name': name,
            'postbox': postbox,
        }).replace('OK, ID - > ', '')

    def logonValidate(self, ValidateCode):
        '''
        登录验证:
        ValidateCode :验证码
        '''
        return self.reqapi(name='login_Email_Verifier_API', parameter={
            'Verification': ValidateCode
        })

    def GetUserData(self):
        '''
        获得用户数据
        '''
        return self.UserData

    def PullingUserData(self):
        '''拉取服务器的用户数据做缓存'''
        self.UserData = json.loads(self.reqapi(name='get_user_data', parameter={}))

    def UploadOtherData(self):
        '''
        上传用户数据
        '''
        return self.reqapi(name='GetorChange_other_user_data', parameter={
            'key': self.OtherKey,
            'id': self.OtherID,
            'v': json.dumps(self.OtherData),
        })

    def PullingOtherData(self):
        '''
        拉取服务器的用户数据
        '''
        self.OtherData = json.loads(self.reqapi(name='GetorChange_other_user_data', parameter={
            'key': self.OtherKey,
            'id': self.OtherID,
        }))
        return self.OtherData

    def Change_user_data(self, data):
        '''更改服务器上的用户数据(昵称之类的)'''
        self.reqapi(name='Change_user_data', parameter={'data': json.dumps(data)})
