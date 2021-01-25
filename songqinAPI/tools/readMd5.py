# -*- coding:utf-8 -*-
# autu :liyongbing  
# time: 2021/1/15
import hashlib


def get_md5(pwd):
    # 创建实例化加密对象
    md5 = hashlib.md5()
    # 进行加密操作
    md5.update(str(pwd).encode('utf-8'))
    # 返回加密后结果  --16进制
    return md5.hexdigest()
