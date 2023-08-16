import requests
import json
def send_api_request(instruction_set:list, 
                     session_id:str,
                     global_params:dict = {},
                     ModName = 'free_other',ApiName = 'instruct',
                     server_address = None,
                     ):
    '''
    Send request to mod with instrumentsAPI
    >>> global_params = {'参数名':'参数值'} # 注意是指令全局参数
    '''
    # 将全局指令参数添加到每个指令的instruction_parameters字段中
    if (not server_address):
        raise Exception('未知服务器地址')
    for instruction in instruction_set:
        if type(instruction) == str:
            break
        instruction['instruction_parameters'].update(global_params)

    params = {
        'ModName': ModName,
        'ApiName': ApiName,
        'instruction_set': json.dumps(instruction_set),
        'SessionID': session_id
    }
    # 发送请求
    response = requests.post(f'{server_address}/api/mod', params=params)

    # 处理响应
    if response.status_code == 200:
        # 解析并返回响应数据
        return response.json()
    else:
        # 处理请求错误
        return f'E url:{response.url}'
    

r =  send_api_request(session_id='1eaad741-93bc-4ff9-82da-97fa3733b4a4',
                 ModName='plugin_market',
                 instruction_set=[
                     {"instruction_name":"new_plugin","instruction_parameters":{
                         'github_publishing':'https://github.com/MCSLTeam/Plugins_is_Star_weaving_agent_download/releases/download/v1.0/Star_weaving_agent_download.rar',
                         'readme':'插件的一个例子（星织写的），本插件用于代理下载文件',
                         'Cloth':'https://www.df100.ltd/portrait.php',
                         'config':'''
{
    "plugin_name": "Star_weaving_agent_download",
    "version": "1.0",
    "description": "星织代理下载",
    "icon": "Cloth.png",
    "author": "星织",
    "author_email": "rc@163.com",
    "on_new_thread": true
  }''' 
                     }}
                 ]
                 ,server_address='http://127.0.0.1:11429')

print(r)
