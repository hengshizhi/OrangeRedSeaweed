# 会话
import time
import uuid
import json
try:
    from .db import mysql as db
except:
    import db.mysql as db

get_session = db.get_session #数据库会话
session_db = db.table.session #关联会话数据表

class session():
    data = {}
    def __init__(self,session_key):
        self.key = session_key #保存key
        # self.get()
    def create(self): #创建sessionkey
        '''
        Create session
        Create a session key is available
        -> session key
        '''
        with get_session() as s:
            session = db.table.session()
            # print(str(uuid.uuid4()))
            session.id = str(uuid.uuid4()) #生成唯一id
            session.created_at = time.time()
            session.updated_at = time.time()
            s.add(session)
            s.commit()
            self.key = session.id
            return session.id
    def getDB(self): #得到数据库里面的session
        with get_session() as s:
            self.data = s.query(session_db).filter(session_db.id == self.key,
            session_db.deleted_at==None).first().dobule_to_dict()['data'] # 查询数据库
            print('DATA:',s.query(session_db).filter(session_db.id == self.key,
            session_db.deleted_at==None).first().dobule_to_dict())
            if(self.data != None):
                self.data = json.loads(self.data) #编码成json
            else:
                self.data = {}
    def refresh(self): 
        '''刷新session,将内存里面的session提交到数据库'''
        with get_session() as s:
            s.query(session_db).filter(session_db.id == self.key).update({'data': json.dumps(self.data),
                                                                             'updated_at':time.time()})
    def Set(self,key,value):
        try:self.data[key] = value
        except:
            self.data['Verification'] = None
            self.data[key] = value
    def delete(self,key):
        '''删除session值:
        session = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
        > key=['a', 'c']
        > session
        {'b': 2, 'd': 4}
        > key = 'b'
        > session
        {'d': 4} 
        '''
        if(str(type(key)) == "<class 'list'>"):
            for i in key:
                del self.data[i]
        else:
            del self.data[key]
    def get(self, key):
        try:return self.data[key]
        except:return None
