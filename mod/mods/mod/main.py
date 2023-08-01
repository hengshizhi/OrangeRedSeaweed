import json
import os

import sdk.other as other
from sanic.response import HTTPResponse
from fileApi.route import main as route


from .ModInformation import information
from .ModInformation import logo as Ilogo
from .ModInformation import modlist
from .ModJs import modjs as modjsObj

def AtRuntimeForTheFirstTime():
    ''' Functions that will be executed every time the program runs mod '''

def main(api):
    return {'Modlist': apiModlist,
            'modjs': apiModjs,
            'logo': logo,
            'GetInformation': GetInformation,
            'management_interface':management_interface
            }

def management_interface(get_or_post, EnableSession, rep, **para):
    s = EnableSession()
    try:
        OT = other.Main('CoreConfiguration', True, s.data['login_status_id'])
    except:
        return rep('You are not logged in')
    if (OT.AdministratorVerification(s)):  # Administrator verification
        with open('./mod/mods/{ModName}/management_interface.html'.format(ModName=get_or_post('management_interface_mod_name')),'r',encoding='utf-8') as f:
            return rep(HTTPResponse(f.read(),content_type='text/html'))
    else:
        return rep('You not is administrators')

def apiModlist(get_or_post, EnableSession, rep, **para):
    s = EnableSession()
    try:
        OT = other.Main('CoreConfiguration', True, s.data['login_status_id'])
    except:
        return rep('You are not logged in')
    if (OT.AdministratorVerification(s)):  # Administrator verification
        return rep(json.dumps(modlist()))
    else:
        return rep('You not is administrators')


def apiModjs(get_or_post, EnableSession, rep, **para):
    return rep(modjs())


def apiDelmod(get_or_post, EnableSession, rep, **para):
    pass


def apiAddmod(get_or_post, EnableSession, rep, **para):
    pass


def apiDisableMod(get_or_post, EnableSession, rep, **para):
    pass


def BackgroundManagement(get_or_post, EnableSession, rep, **para):
    '''后台管理'''


def logo(get_or_post, EnableSession, rep, **para):
    '''mod logo'''
    modName = get_or_post('LogoModName')
    logos = Ilogo(modName)
    return rep(HTTPResponse(logos, content_type='image/jpeg'))


def GetInformation(get_or_post, EnableSession, rep, **para):
    modName = get_or_post('LogoModName')
    inf = information(modName)
    return rep(json.dumps(inf))


def modjs() -> str:
    ret = '''

/**
 * 获取 cookie 对象
 * @returns  cookie 键值对对象
 */
function getCookieObject() {
    let cookieString = document.cookie;
    cookieString = cookieString.substring(0, cookieString.length - 1);
    let tempCookieArray = cookieString.split('; ');

    let cookieObject = {}; // 存放 cookie 键值对

    tempCookieArray.forEach(item => {
        let name = item.substring(0, item.indexOf('='));
        let value = item.substring(item.indexOf('=') + 1);
        value = decodeURIComponent(value); // 还原字符串
        cookieObject[name] = value; // 将键值插入中这个对象中
    });

    return cookieObject // 返回包含 cookie 键值对的对象
}
function _sendAPIRequest(url, data, successCallback, errorCallback) {
  $.ajax({
    url: url,
    type: 'POST',
    data: data,
    contentType: 'application/json',
    success: function(response) {
      if (successCallback && typeof successCallback === 'function') {
        successCallback(response);
      }
    },
    error: function(xhr, status, error) {
      if (errorCallback && typeof errorCallback === 'function') {
        errorCallback(xhr, status, error);
      }
    }
  });
}

// url：API的URL。
// data：要发送给API的数据。
// successCallback：成功回调函数，它将在API请求成功时被调用，并将API的响应作为参数传递给它。
// errorCallback：失败回调函数，它将在API请求失败时被调用，并将XHR对象、错误状态和错误信息作为参数传递给它。
// function handleSuccess(response) {
//     console.log('API请求成功！');
//     console.log('响应数据：', response);
//   }
  
//   // 自定义失败回调函数
//   function handleError(xhr, status, error) {
//     console.log('API请求失败！');
//     console.log('错误状态：', status);
//     console.log('错误信息：', error);
//   }
  
//   // 调用API请求
//   var apiUrl = 'https://api.example.com';
//   var requestData = { name: 'John', age: 30 };
  
//   sendAPIRequest(apiUrl, requestData, handleSuccess, handleError);

function get_param_value(paramName) {
    var reg = new RegExp("(^|&)" + keyword + "=([^&]*)(&|$)", "i");
    var r = window.location.search.substr(1).match(reg);
    if (r != null) return unescape(r[2]);
    return null;
}

// 示例使用：
// var name = get_param_value('name'); // 获取名为"name"的参数值
// var age = get_param_value('age'); // 获取名为"age"的参数值
'''
    modlsit = modlist()
    for k, v in modlsit.items():
        Modjs = modjsObj(k)
        ret += Modjs.output()
    return ret


def delmod():
    pass


def addmod():
    pass


def DisableMod():
    '''禁用原理:改mod路径名'''
