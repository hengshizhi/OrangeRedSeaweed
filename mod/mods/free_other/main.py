#This module envisions a free other data API that utilizes caching to save other objects, 
#and then utilizes a series of specific
#Instructions (sets) can be used to manipulate objects, 
#all of which can be accomplished through APIs
#You need to first request a function such as new to create an object 
#and get the cache location of the object
#Then use functions such as' operate 'to manipulate the instruction set
#With this thing, 
#you can safely and quickly manipulate data without writing Python (only JS SDK is left)
#Only the JS SDK is left, and the SDK is also universal, just write it once
from sdk.other import Main as other
from sdk.other import CoreConfiguration as ccf
import uuid
import json
from InitialLoading import Cache as Cache
import sdk.instructs.api_func as instructs_api_func
import mod.mods.free_other.instructs_func as instructs_func
def AtRuntimeForTheFirstTime():
    pass
def main(api):
    api['free_other_session_new'] = free_other_session_new
    api['free_other_user_id_new'] = free_other_user_id_new
    api['instruct'] = instruct
    return api

def new_free_other_session(KEY, user_id=None, session='None'):
    obj = other(KEY,session=session,USERID=user_id)
    cache_name = str(uuid.uuid4())
    Cache.NewCache(cache_name,lambda :obj) # 新建缓存保存对象
    return cache_name

def free_other_session_new(get_or_post, enable_session, rep, **para):
    '''Creating a "free_other"'s session, returning 'free_other' the Session ID
    'free_other' The session ID corresponds to the cache name'''
    return rep(json.dumps({'free_other_session':new_free_other_session(get_or_post('key'),session=enable_session())}))

def free_other_user_id_new(get_or_post, enable_session, rep, **para):
    '''Create a "free_other" session using "user_id", 
    provided that you have an administrator's session or that "user_id" is your own'''
    if (ccf(session=enable_session()).administrators):
        return rep(json.dumps({'free_other_session':new_free_other_session(get_or_post('key'),user_id=get_or_post('user_id'))}))
    else:
        return free_other_session_new(get_or_post, enable_session, rep, **para)

def instruct(get_or_post, enable_session, rep, **para):
    instruction_name_list = ['Pulling','SubmitToDatabase','AdministratorVerification','get_data','change']
    instruction_func_list = instructs_func
    dependency_table = {
        'get_data':['Pulling'],
        'SubmitToDatabase':['change'],
        'AdministratorVerification':['Pulling']
    }
    return instructs_api_func.func(get_or_post, enable_session, rep,instruction_name_list,instruction_func_list,dependency_table)