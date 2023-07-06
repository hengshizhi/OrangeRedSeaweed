# Other Data SDKs
import json
from sanic.response import text
from operation.user import GET_other_user_data_interior , Change_other_user_data_interior
class Main():
    def __init__(self, KEY, UseJson: bool = True, USERID=2, session=False,) -> None:
        '''
        Other can store any common data type supported by Python, except for objects
        Precautions for use:
            1. Pulling() is required to obtain data
            2. Uploading data requires executing SubmitToDatabase()
            3. AdministratorVerification() can perform administrator verification, which verifies whether this Other is owned by the administrator
            4. UserLoginAuthentication() can perform login authentication
        parameter:
            KEY :The JSON key name in the data field
            UseJson :obsolete（已废弃）
            USERID: User ID (2id is the super administrator ID, and non user data should be placed here)
            session: Session can be used to obtain logged in users_id ()
        '''
        if (bool(session)):
            try:
                self.id = session.data['login_status_id']
            except:
                self.id = None
        else:
            self.id = USERID
        self.key = KEY
        self.data = None
        # return ID

    def Pulling(self) -> bool:
        '''Pull data from the database to self.data'''
        self.data = GET_other_user_data_interior(user_id=self.id, id=self.key)
        if (self.data == None): self.data = {}
        return True

    def SubmitToDatabase(self) -> bool:
        '''Submit the content of self.data to the database'''
        Change_other_user_data_interior(user_id=self.id, id=self.key, v=self.data)
        return True

    def GetKeyData(self, key) -> int | None | str | dict:
        '''Obtain data for the key value specified in self.data'''
        try:
            return self.data[key]
        except KeyError:
            return None

    def AdministratorVerification(self, Session: object) -> bool:
        '''Administrator verification function, 
            returning 'None' indicates not logged in, 
            returning 'true' indicates administrator, 
            returning 'false' indicates not logged in
        Parameters:
            Session: Objects returned using the 'EnableSession' function
        '''
        if (not self.UserLoginAuthentication(Session)): return None
        self.Pulling()
        try:
            if (self.data['administrators']):
                return True
            else:
                return False
        except:
            return False

    def UserLoginAuthentication(self, Session: object) -> bool:
        '''User login verification, 
        if login returns id, 
        if not logged in returns none
        Parameter: Session: Objects returned using the 'Enabling Session' function  '''
        try:
            return Session.data['login_status_id']  # Obtain login status
        except:
            return None  # Not Logged In


class CoreConfiguration:
    administrators = None  # 管理员
    ContentEditingRights = None  # 内容编辑权
    PermissionList = [administrators, ContentEditingRights]  # 权限列表

    def __init__(self, user_id=2, session=False, Pulling=True, OT=False) -> None:
        '''
        '(class) CoreConfiguration' is used for editing, modifying, and viewing core configurations
        parameter :
            user_id: User ID
            session: Session can be used to obtain logged in users_id (User_ ID acquisition priority: OT>Session>Inheritance)
            Pulling: Whether to automatically pull the database configuration when instantiating a class (optional)
            OT :other.Main object (optional) ,can use the already created other.Main object
        class variable :
            administrators : administered limits of authority
            ContentEditingRights : content editin rights's limits of authority
            PermissionList : use limits of authority's list
        '''
        if (bool(OT)):
            if (user_id == None or user_id == 2): raise Exception('请传入正确的 user_id 参数')
            self.OT = Main(KEY='CoreConfiguration', USERID=user_id)  # 加载用户数据
        elif (bool(session)):
            self.OT = Main(KEY='CoreConfiguration', session=session)  # 加载用户数据
        else:
            self.OT = OT
        if (Pulling): self.PullingDatabase()

    def PullingDatabase(self):
        '''Pull permission information'''
        self.OT.Pulling()
        self.administrators = self.OT.GetKeyData('administrators')
        self.ContentEditingRights = self.OT.GetKeyData('ContentEditingRights')

    def submitTo(self):
        '''Submit to database'''
        self.OT.data = {'administrators': self.administrators, 'ContentEditingRights': self.ContentEditingRights}
        return self.OT.SubmitToDatabase()


def ValidateLogon(s):
    '''登录验证使用，传入Session object'''
    try:
        a = s.data['login_status_id']
        del a
        return [True, s.data['login_status_id']]
    except:
        return [False, None]
