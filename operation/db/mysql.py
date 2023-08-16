import contextlib

from sqlalchemy import (
    create_engine,
)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from . import config as config
from . import table as table_data

# import config as  config # config模块里有自己写的配置，我们可以换成别的，注意下面用到config的地方也要一起换
# import table as table_data #所有表
engine = create_engine(
    config.SQLALCHEMY_DATABASE_URI,  # SQLAlchemy 数据库连接串，格式见下面
    echo=bool(config.SQLALCHEMY_ECHO),  # 是不是要把所执行的SQL打印出来，一般用于调试
    pool_size=int(config.SQLALCHEMY_POOL_SIZE),  # 连接池大小
    max_overflow=int(config.SQLALCHEMY_POOL_MAX_SIZE),  # 连接池最大的大小
    pool_recycle=int(config.SQLALCHEMY_POOL_RECYCLE),  # 多久时间回收连接
)

Session = sessionmaker(bind=engine)
Base = declarative_base()  # 生成orm基类


@contextlib.contextmanager
def get_session():
    s = Session()
    try:
        yield s
        s.commit()
    except Exception as e:
        s.rollback()
        raise e
    finally:
        s.close()


class table():  # 表类
    class User(table_data.User, Base): pass

    class session(table_data.session, Base): pass

    class OTHERDATA(table_data.OTHERDATA, Base): pass

    class other_data_user_key_index(table_data.other_data_user_key_index, Base): pass


try:
    Base.metadata.create_all(engine) #创建表结构
    pass
except:
    print('数据库连接错误')
    exit('DATABASE_CONNECTION_ERROR')
