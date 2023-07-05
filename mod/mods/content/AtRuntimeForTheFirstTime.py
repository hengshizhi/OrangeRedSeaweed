import json

import fileApi.PathInfo as PathInfo
import fileApi.route as route
from InitialLoading import Cache as Cache
from mod.mods.content.content import ContentAliasesCorrespondUsersID


def AtRuntimeForTheFirstTime():
    ''' Functions that will be executed every time the program runs mod '''
    Cache.NewCache('ContentAliasesCorrespondUsersID', ContentAliasesCorrespondUsersID)  # 储存缓存
    route.mkdir('./ContentTemplate')
    from mod.mods.content.ORSCFS import ContentTemplate as ContentTemplates
    for k, v in PathInfo.Dict('./ContentTemplate/', './ContentTemplate/').items():  # 遍历模板目录
        if ('.ORStemplate.json' in k):
            with open(v[1], 'r', encoding='utf-8') as template:
                ContentTemplates[k.replace('.ORStemplate.json', '')] = json.loads(template.read())
