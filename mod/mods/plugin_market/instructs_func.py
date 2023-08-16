from InitialLoading import Cache
import json
from sdk.instructs import instruction_parameters
from sdk.other import Main as other
import time
from operation.user import Traverse_other_data_with_the_same_key_value
def test_and_verify(d):
    if (type(d) != list):
        if (d == '' or d == None):return False
        return True
    else:
        for i in d:
            if (i == '' or i == None):return False
            return True
def traversal_judgment(data:list,conditions:object):
    t = 0
    for i in data:
        if conditions(i):
            t += 1
    if len(data) == t:
        return True
    return False
def record_publishing(github_publishing,author,plugin_name,version,plugin_description,Cloth,readme,other:other):

    if (not test_and_verify([author,plugin_name,version])):
        return 'Incomplete configuration file'
    if type(other.data) != list:
        other.data = []
    else:
        for i in other.data:
            if (i['plugin_name'] == plugin_name and i['version'] == version):
                return 'Prohibit publishing plugins of the same version'
    other.data.append({
        'plugin_name':plugin_name,
        'version':version,
        'plugin_description':plugin_description,
        'Cloth':Cloth,
        'readme':readme,
        'author':author,
        'examine':False,
        'github_publishing':github_publishing,
        'release_time':time.time()
    })
    other.SubmitToDatabase()
    return True

def new_plugin(parameters:instruction_parameters):
    plugin_config = json.loads(parameters.get('config'))
    github_publishing = parameters.get('github_publishing')
    readme = parameters.get('readme')
    Cloth = parameters.get('Cloth')
    _other = parameters.get('other')
    if ('releases' in github_publishing and 'https://github.com' in github_publishing):
        if (not plugin_config['version']):
            version = github_publishing.split('/')[-2]
        else:
            version = plugin_config['version']
        return record_publishing(github_publishing,plugin_config['author'],plugin_config['plugin_name'],version,plugin_config['description'],Cloth,readme,_other)
    else:
        return 'Not a publishing link'

def search_plugin(parameters:instruction_parameters):
    def organize_into_list(d:dict):
        ret = []
        for k,v in d.items():
            for i in v:
                if (i['examine']):
                    del i['examine']
                    ret.append(i)
        return ret
    plugin_data = organize_into_list(Traverse_other_data_with_the_same_key_value('pi'))
    def s_field(s,field,data):
        ret = []
        if (field == 'global'):
            for i in data:
                for k,v in i.items():
                    if (s in v):
                        ret.append({'data':i,'according to':field})
                        break
        else:
            for i in plugin_data:
                if (s in i[field]):
                    ret.append({'data':i,'according to':field})
        return ret
    _other = parameters.get('other')
    _s = parameters.get('s').split(' ') # Search Term,Separate keywords with spaces
    _type = parameters.get('type').split(' ') # Search type
    # Search types include: Global, Author, Introduction, Readme, Plugin Name, Release Time, and Version
    # If it is global, the default sorting order is: plugin name, introduction, readme, author, version, and release time
    if (_s == ['']):
        return plugin_data
    elif (len(_s) != len(_type)):
        return 'The search term does not correspond to the search type'
    else:
        rep = plugin_data
        for i in range(len(_s)):
            if (_type[i] in ['plugin_name','version','plugin_description','Cloth','version','global','author']):
                rep = s_field(_s[i],_type[i],rep)
        if (rep == plugin_data):
            return '纳尼？好奇怪'
        return rep
    