def main(api):
    api['helloWrold'] = helloWrold
    return api
def helloWrold(get_or_post,EnableSession,rep,**para):
    s = EnableSession()
    s.data['hello'] = 'yes'
    s.refresh()
    get = get_or_post('hello','没有啦')
    return rep(f'OK啦!GET:{get}',s)