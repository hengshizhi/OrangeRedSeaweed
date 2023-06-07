def main(api):
    api['helloWrold'] = helloWrold
    return api
def helloWrold(get_or_post,EnableSession,rep,**para):
    s = EnableSession()
    s.data['hello'] = 'yes'
    s.refresh()
    return rep('OK啦!',s)