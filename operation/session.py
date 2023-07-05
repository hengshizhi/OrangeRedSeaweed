# 会话
import time
import uuid
import json

try:
    from .md5 import get_md5
    from .db import mysql as db
except:
    import db.mysql as db
    from md5 import get_md5

get_session = db.get_session  # Database Session
session_db = db.table.session  # Associate Session Data Table


class session():
    data = {}

    def __init__(self, session_key=None):
        if (session_key != None):
            self.key = session_key

    def create(self):
        '''
        Create session
        Create a session key is available
        -> session id
        '''
        with get_session() as s:
            session = db.table.session()
            uuidsuiji = str(uuid.uuid4())
            session.id = get_md5(uuidsuiji)
            session.created_at = time.time()
            session.updated_at = time.time()
            s.add(session)
            s.commit()
            self.key = uuidsuiji
            return session.id

    def getDB(self):
        '''Obtain the session in the database'''
        with get_session() as s:
            self.data = s.query(session_db).filter(session_db.id == self.GetMd5SessionId(),
                                                   session_db.deleted_at == None).first().dobule_to_dict()[
                'data']  # query data base
            if (self.data != None):
                self.data = json.loads(self.data)
            else:
                self.data = {}

    def Pulling(self):
        '''Pull the content of the database'''
        self.getDB()

    def GetMd5SessionId(self):
        '''Get Md5's Session id'''
        return get_md5(self.key)

    def refresh(self):
        '''Refresh the session and submit the session in memory to the database'''
        with get_session() as s:
            s.query(session_db).filter(session_db.id == self.GetMd5SessionId()).update(
                {'data': json.dumps(self.data), 'updated_at': time.time()})

    def SubmitTo(self):
        '''Submit session data from self.data to the database'''
        self.refresh()

    def Set(self, key, value):
        try:
            self.data[key] = value
        except:
            self.data['Verification'] = None
            self.data[key] = value

    def delete(self, key):
        '''Delete session value:
        session = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
        > key=['a', 'c']
        > session
        {'b': 2, 'd': 4}
        > key = 'b'
        > session
        {'d': 4} 
        '''
        if (type(key) == list):
            for i in key:
                del self.data[i]
        else:
            del self.data[key]

    def get(self, key):
        try:
            return self.data[key]
        except:
            return None
