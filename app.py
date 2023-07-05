import os
import sys

sys.path.append(os.getcwd() + '/operation/')
sys.path.append(os.getcwd() + '/sdk/')
sys.path.append(os.getcwd() + '/fileApi/')
try:
    from sanic import Sanic
    from sanic.response import text, html, json, file, raw, file_stream, redirect, empty  # 导入sanic web的工具类
    import api as api_main
except:
    # import autoinstall
    from sanic import Sanic
    from sanic.response import text, html, json, file, raw, file_stream, redirect, empty  # 导入sanic web的工具类
    import api as api_main
from MainConfig import HttpServerConfig as config  # 定位配置文件


def get_or_post(request, key):  # If there is no GET parameter, use post
    if (request.args.get(key) != None):
        return request.args.get(key)
    elif (request.form.get(key) != None):
        return request.form.get(key)
    return None


app = Sanic("OrangeRedSeaweed")  # Instantiating Sanic


async def favicon(request):
    '''Favicon.ico icon'''
    import MainConfig
    return await file(MainConfig.favicon)


async def api(request, name):  # API执行函数
    data = api_main.main(request, name)
    print(data)
    ret = data['data']
    try:
        for k, v in data['cookie'].items():  # 设置cookie
            ret.cookies[k] = v
    except:
        pass
    try:
        if (data['async']):
            return await ret
        else:
            return ret
    except:
        return ret


async def front_end(request, path):
    '''前端'''
    try:
        return await file('./front_end/' + path)
    except:
        return await file('./front_end/index.html')


app.add_route(front_end, f'/<path:path>', methods=['GET', 'POST'])  # front_end
app.add_route(api, f'/api/<name:path>', methods=['GET', 'POST'])  # HTTPAPI
app.add_route(favicon, "/favicon.ico", methods=["GET"])  # favicon.ico

if __name__ == "__main__":
    app.run(host=config['host'], port=config['port'], debug=config['debug'], dev=config['dev'])
