from sdk.other import Main as other
import json
from sdk.instructs import run as instructs_run
def func(get_or_post, enable_session, rep,instruction_name_list,instruction_func_list,dependency_table):
    session = enable_session()
    if other('CoreConfiguration',session=session).UserLoginAuthentication(session):
        instruction_set = json.loads(get_or_post('instruction_set'))
        return rep(json.dumps(instructs_run(instruction_set,instruction_name_list,instruction_func_list,dependency_table)))
    else:
        return rep(json.dumps(['You are not logged in']))