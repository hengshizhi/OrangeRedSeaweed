from sdk.other import Main as other
import json
from sdk.instructs import run as instructs_run
def func(get_or_post, enable_session, rep,
         instruction_name_list:list,
         instruction_func_list:object|list,
         dependency_table:dict,
         logged:bool = True):
    '''
    >>> return func(get_or_post, enable_session, rep,instruction_name_list,instruction_func_list,dependency_table)
    instruction_name_list: 指令名列表（支持的指令的列表）
    instruction_func_list: 指令函数列表，需要与指令名列表对应，如果传入的是类或者模块，将从里面挑选和指令名一致的函数来执行
    dependency_table: 指令的依赖关系表{'<指令名>':['依赖项指令1','依赖项指令2']}
    logged :是否需要登录（bool）
    '''
    if (logged):
        session = enable_session()
        if other('CoreConfiguration',session=session).UserLoginAuthentication(session):
            instruction_set = json.loads(get_or_post('instruction_set'))
            return rep(json.dumps(instructs_run(instruction_set,instruction_name_list,instruction_func_list,dependency_table)))
        else:
            return rep(json.dumps(['You are not logged in']))
    else:
        instruction_set = json.loads(get_or_post('instruction_set'))
        return rep(json.dumps(instructs_run(instruction_set,instruction_name_list,instruction_func_list,dependency_table)))