# MD5算法
import hashlib


def get_md5(data):  # 传参为需要加密的字符串
    hl = hashlib.md5()
    hl.update(data.encode("utf-8"))
    return hl.hexdigest()
