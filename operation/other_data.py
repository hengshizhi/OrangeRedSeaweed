from operation.user import get_user_data , Change_user_data
import time as time
import db.mysql as db
import md5 as md5

from InitialLoading import Cache # 导入缓存

get_session = db.get_session
otherdata = db.table.OTHERDATA
oduki = db.table.other_data_user_key_index # other_data_user_key_index 表

def Pre_load_cache():
    global oduki
    def chouqv(data):
        ret = {}
        shangcejieguo = None # 上一次检查的
        for i in data:
            i = i.dobule_to_dict()
            try:
                ret[i['user_id']][i['ot_key']] = i['index']
            except:
                ret[i['user_id']] = {}
                ret[i['user_id']][i['ot_key']] = i['index']
        return ret
            # if shangcejieguo == i['user_id']:
            #     ret[i['user_id']][i['ot_key']] = i['index']
            # else:
            #     shangcejieguo = i['user_id']
            #     ret[i['user_id']] = {}
            #     ret[i['user_id']][i['ot_key']] = i['index']
    class _oduki():
        def __init__(self,oduki:oduki) -> None:
            self.oduki = oduki
            with get_session() as s:
                data = s.query(self.oduki).all()
                self.data = chouqv(data)
    
    _oduki(oduki)


def e(obj):
    try:
        return obj()
    except:
        return False

def new_user_key(user_id=False,ot_key='',data={}):
    '''为一个用户新增一个键值'''
    global oduki
    global otherdata
    with get_session() as s:
        if user_id and ot_key and not e(lambda:s.query(oduki).filter(oduki.user_id ==user_id , oduki.ot_key == ot_key).one()):

            index = int(time.time())
            _oduki = oduki()
            _oduki.user_id = user_id
            _oduki.ot_key = ot_key
            _oduki.index = index
            _oduki.created_at = time.time()
            s.add(_oduki)
            s.commit()
            with get_session() as s1:
                _otherdata = otherdata()
                _otherdata.index = index
                _otherdata.data = str(data)
                _otherdata.created_at = time.time()
                s1.add(_otherdata)
                s1.commit()
            return True
        else:
            raise Exception("You really 6,don't play tricks of killing yourself")
def new_GOUDI(user_id=False,ot_key=''):
    '''获得用户其他数据
    user_id:用户id
    key:其他数据中的键值(必填)
    '''
    if user_id and ot_key:
        with get_session() as s:
            # 没有:None
            data = s.query(oduki).filter(oduki.user_id ==user_id , oduki.ot_key == ot_key).one_or_none()
            if not data:
                return data
            return data

# new_GOUDI('111','11111')
# new_user_key('1111','8727827')
# Pre_load_cache()


































def GET_other_user_data_interior(user_id=False, name=False, postbox=False, id: str = ''):
    '''获得用户其他数据(DATA字段)
    id :其他数据中的键值
    '''
    # data = json.loads(get_user_data(id=user_id,name=name,postbox=postbox)['DATA'])
    # return data[id]
    try:
        data = get_user_data(id=user_id, name=name, postbox=postbox)['DATA']
        data = eval(data)
    except:
        data = {}
        data[id] = None
        Change_user_data(id=user_id, data={'DATA': str(data)})  # 更新用户数据
        return data[id]
    try:
        return data[id]
    except:  # 假如没有创建键
        data[id] = None
        Change_user_data(id=user_id, data={'DATA': str(data)})  # 更新用户数据
    return data[id]


def Change_other_user_data_interior(user_id=False, name=False, postbox=False, id: str = '', v: str = ''):
    '''
    更改用户其他数据(DATA字段)
    parameter :
        v: 要更新的数据(json)
    '''
    try:
        data = eval(get_user_data(id=user_id, name=name, postbox=postbox)['DATA'])
    except:  # 没有使用过其他用户数据的情况
        data = {}
        data[id] = None
        data[id] = v  # 保存键
        Change_user_data(id=user_id, data={'DATA': str(data)})  # 更新用户数据
        return str(data[id])
    try:
        data[id] = v  # 保存键
        Change_user_data(id=user_id, data={'DATA': str(data)})  # 更新用户数据
    except:  # 假如没有键值则创造键值
        data[id] = None
        data[id] = v  # 保存键
        Change_user_data(id=user_id, data={'DATA': str(data)})  # 更新用户数据
    return str(data[id])
