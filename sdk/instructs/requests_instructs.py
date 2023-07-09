import requests
import json
def send_api_request(instruction_set:list, 
                     session_id:str,
                     global_params:dict,
                     ModName = 'free_other',ApiName = 'instruct'):
    '''
    Send request to mod with instrumentsAPI
    >>> global_params = {'参数名':'参数值'} # 注意是指令全局参数
    '''
    # 将全局指令参数添加到每个指令的instruction_parameters字段中
    for instruction in instruction_set:
        instruction['instruction_parameters'].update(global_params)

    params = {
        'ModName': ModName,
        'ApiName': ApiName,
        'instruction_set': json.dumps(instruction_set),
        'SessionID': session_id
    }
    # 发送请求
    response = requests.post('/api/mod', params=params)

    # 处理响应
    if response.status_code == 200:
        # 解析并返回响应数据
        return response.json()
    else:
        # 处理请求错误
        return None