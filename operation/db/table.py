# 储存表结构
from sqlalchemy import (
    Column,
    Integer,
    DateTime,
    String,
    TIMESTAMP
)


class BaseMixin:
    """model的基类,所有model都必须继承"""
    created_at = Column(DateTime, nullable=False)
    updated_at = Column(TIMESTAMP, nullable=False)
    deleted_at = Column(Integer)  # 可以为空, 如果非空, 则为软删
    def single_to_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}

    # 多个对象
    def dobule_to_dict(self):
        result = {}
        for key in self.__mapper__.c.keys():
            if getattr(self, key) is not None:
                result[key] = str(getattr(self, key))
            else:
                result[key] = getattr(self, key)
        return result


class User(BaseMixin):
    __tablename__ = "user"  # 表名
    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String(32), nullable=False)  # 用户名
    Key = Column(String(64), nullable=False)  # 密码
    Registration_time = Column(Integer)  # 注册时间
    postbox = Column(String(64), nullable=False)  # 邮箱
    nickname = Column(String(32))  # 昵称
    HeadPortrait = Column(String(32))  # 头像(url)
    # mail_validation = Column(Integer,nullable=False,server_default='0') # 是否验证了电子邮件
    # banned = Column(Integer,nullable=False,server_default='0') # 是否封禁
    LastLogin = Column(Integer)  # 上次登录时间
    DATA = Column(String(50000))  # 其他用户数据储存地


class session(BaseMixin):  # 会话
    __tablename__ = "session"  # 表名
    # key = Column(String(64),nullable=False,primary_key=True)
    id = Column(String(64), nullable=False, primary_key=True)
    data = Column(String(255), server_default='{}')  # 会话内容

class OTHERDATA(BaseMixin):
    '''其他数据数据表'''
    __tablename__ = "otherdata"  # 表名
    index = Column(Integer, nullable=False, primary_key=True,comment='数据索引')
    data = Column(String(255), comment='数据本体')  # 会话内容

class other_data_user_key_index(BaseMixin):
    '''其他数据用户键索引'''
    __tablename__ = "other_data_user_key_index"  # 表名
    user_id = Column(Integer,  nullable=False ,comment='用户名')
    ot_key = Column(Integer, nullable=False ,comment='其他数据的键')
    index = Column(Integer, nullable=False, primary_key=True , comment='数据索引') # 对应OTHERDATA的index