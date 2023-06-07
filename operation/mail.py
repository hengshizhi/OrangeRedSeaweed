import smtplib
from email.mime.text import MIMEText
from email.header import Header
try:
    # import config #导入配置
    from config import main_config as main_config
    config = main_config()
except:
    from .config import main_config as main_config
    config = main_config()
class mail():
    def __init__(self):
        self.connection()
    def connection(self):
        # 创建 SMTP 对象
        self.smtp = smtplib.SMTP()
        # 连接（connect）指定服务器
        self.smtp.connect(config.connect, port=25)
        # 登录，需要：登录邮箱和授权码
        self.smtp.login(user=config.user, password=config.password)
    def send(self,content,theme,target:dict):
        '''发送邮件：
        content：邮件内容
        theme：邮件主题
        target['nickname']：收件人昵称
        target['address']：收件人地址
        '''
        # 构造MIMEText对象，参数为：正文，MIME的subtype，编码方式
        message = MIMEText(content, config.MIME, config.encoding)
        message['From'] = Header(config.nickname, config.encoding)  # 发件人的昵称
        message['To'] = Header(target['nickname'], config.encoding)  # 收件人的昵称
        message['Subject'] = Header(theme, config.encoding)  # 定义主题内容
        # print(message)
        try:
            self.smtp.sendmail(from_addr=config.from_addr, to_addrs=target['address'], msg=message.as_string())
        except:
            self.connection()
            self.smtp.sendmail(from_addr=config.from_addr, to_addrs=target['address'], msg=message.as_string())
# main = mail()
# main.send('你要干嘛','哈哈哈',{'nickname':'xingzhi','address':'xh-xhsz@foxmail.com'})
