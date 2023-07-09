from InitialLoading import Cache
import json
from sdk.instructs import instruction_parameters
def get_other_instance(free_other_s_id):
    '''Get the other object from the cache instead of creating directly'''
    return Cache.GetCache(free_other_s_id).Pulling()
def Pulling(parameters:instruction_parameters):
    other_instance = get_other_instance(parameters.get('free_other_s_id'))
    return other_instance.Pulling()

def SubmitToDatabase(parameters:instruction_parameters):
    other_instance = get_other_instance(parameters.get('free_other_s_id'))
    return other_instance.SubmitToDatabase()

def AdministratorVerification(parameters:instruction_parameters):
    other_instance = get_other_instance(parameters.get('free_other_s_id'))
    return other_instance.AdministratorVerification()

def get_data(parameters:instruction_parameters):
    other_instance = get_other_instance(parameters.get('free_other_s_id'))
    return other_instance.data

def change(parameters:instruction_parameters):
    other_instance = get_other_instance(parameters.get('free_other_s_id'))
    other_instance.data = json.loads(parameters['data'])
    return other_instance.data