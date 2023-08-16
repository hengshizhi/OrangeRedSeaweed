from sdk.other import Main as other
from sdk.other import CoreConfiguration as ccf
import uuid
import json
from InitialLoading import Cache as Cache
import sdk.instructs.api_func as instructs_api_func
import mod.mods.plugin_market.instructs_func as instructs_func

def main(api):
    api = {
        'instruct':instruct
    }
    return api

def instruct(get_or_post, enable_session, rep, **para):
    g_p = {'other':other('pi',session=enable_session(),Pulling=True)}
    instruction_name_list = ['new_plugin','search_plugin']
    instruction_func_list = instructs_func
    return instructs_api_func.func(get_or_post,
                                    enable_session,
                                    rep,
                                    instruction_name_list,
                                    instruction_func_list,
                                    logged=True,
                                    global_parameters=g_p)
