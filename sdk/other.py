# Other Data SDKs

from user import GET_other_user_data_interior as GET_other_user_data_interior
from user import Change_other_user_data_interior as CHANGE_other_user_data_interior
import json as json
from user import Change_user_data

class Main():
    def __init__(self,KEY,UseJson:bool = True,ID=2,) -> None:
        '''parameter:
            KEY :The JSON key name in the data field
            ID: User ID (2id is the super administrator ID, and non user data should be placed here)
        '''
        self.key = KEY
        self.id = ID
        self.UseJson = UseJson
        if (UseJson):
            self.data = {}
        else:
            self.data = ''
        # return ID
    def Pulling(self) -> bool:
        '''Pull data from the database to self.data'''
        # print(GET_other_user_data_interior(user_id=self.id,id=self.key))
        if (self.UseJson):
            self.data = GET_other_user_data_interior(user_id=self.id,id=self.key)
        else:
            self.data = GET_other_user_data_interior(user_id=self.id,id=self.key)
        return True
    def SubmitToDatabase(self) -> bool:
        '''Submit the content of self.data to the database'''
        if (self.UseJson):json.dumps(CHANGE_other_user_data_interior(user_id=self.id,id=self.key,v=self.data))
        else:CHANGE_other_user_data_interior(user_id=self.id,id=self.key,v=self.data)
        return True
    
