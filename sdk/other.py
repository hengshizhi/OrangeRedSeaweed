# Other Data SDKs

from ..operation.user import GET_other_user_data_interior as GET_other_user_data_interior
from ..operation.user import Change_other_user_data_interior as CHANGE_other_user_data_interior
import json as json

class Main():
    def __init__(self,KEY,UseJson:bool,ID=2,) -> None:
        '''parameter:
            KEY :The JSON key name in the data field
            ID: User ID (2id is the super administrator ID, and non user data should be placed here)
        '''
        self.key = KEY
        self.id = ID
        self.UseJson = UseJson
        return ID
    def Pulling(self) -> bool:
        '''Pull data from the database to self.data'''
        self.data = json.loads(GET_other_user_data_interior(user_id=self.id,id=self.key))
        return True
    def SubmitToDatabase(self) -> bool:
        '''Submit the content of self.data to the database'''
        json.dumps(CHANGE_other_user_data_interior(user_id=self.id,id=self.key,v=self.data))
        return True