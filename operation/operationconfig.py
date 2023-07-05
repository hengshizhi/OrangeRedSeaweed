# openration config
class main_config():
    connect = 'smtp.163.com'  # 服务器地址
    user = 'xh_xhsz@163.com'
    password = 'HDLNJXVEKZUURQUQ'
    nickname = '维度事务所'  # 发件人昵称
    from_addr = 'xh_xhsz@163.com'  # 发件人邮箱
    encoding = 'utf8'  # 编码
    MIME = 'html'  # MIME type
    secret = 'xh_xhsz@163.com'  # 密送人地址


class information():  # 网站信息
    name = 'dflstbols'  # 邮件显示的网站名


class Email_login():
    '''
    配置介绍
    这个配置是邮件模板
    {websiteName} :网站名
    {nickname} :用户昵称
    {name} :用户名
    {Verification} :验证码(如果有)
    '''
    TEMPlate = '''
    <h1>{websiteName}验证码</h1><br>
    你好{nickname}<br>用户名:{name}<br>
    你的验证码是:<b>{Verification}</b><br>
    你本次会话的SessionKey是<b>{SessionKey}</b>
    请注意保管
    '''  # 邮件主体
    Theme = '''
    {websiteName}的验证码
    '''  # 邮件主题


OtherUserDataGetsKey = {

}  # 其他用户数据获取密钥
