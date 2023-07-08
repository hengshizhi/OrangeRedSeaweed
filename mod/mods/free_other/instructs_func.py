from InitialLoading import Cache
def get_other_instance(free_other_s_id):
    '''Get the other object from the cache instead of creating directly'''
    return Cache.GetCache(free_other_s_id).Pulling()
def Pulling(parameters):
    other_instance = get_other_instance(parameters['free_other_s_id'])
    return other_instance.Pulling()

def SubmitToDatabase(parameters):
    other_instance = get_other_instance(parameters['free_other_s_id'])
    return other_instance.SubmitToDatabase()

def AdministratorVerification(parameters):
    other_instance = get_other_instance(parameters['free_other_s_id'])
    return other_instance.AdministratorVerification()

def get_data(parameters):
    other_instance = get_other_instance(parameters['free_other_s_id'])
    return other_instance.data

def change(parameters):
    other_instance = get_other_instance(parameters['free_other_s_id'])
    other_instance.data = parameters['data']
    return other_instance.data