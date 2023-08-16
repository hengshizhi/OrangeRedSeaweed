from operation.user import get_user_data , Change_user_data

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
