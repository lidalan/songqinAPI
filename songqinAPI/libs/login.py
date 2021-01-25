# -*- coding:utf-8 -*-
# autu :liyongbing  
# time: 2021/1/13
import copy
import json
from tools.readMd5 import get_md5
import requests
from config.config import HOST


class Login:
    def login(self,inData, getToken=True):
        url = f'{HOST}/account/sLogin'
        # 修改输入参数password加密结果
        payload = copy.copy(inData)
        payload['password'] = get_md5(payload['password'])
        # 修改后的值

        res = requests.post(url=url, params=payload)

        # res = requests.post(url=url, params=payload, proxies=fiddler)
        if getToken:

            return json.loads(res.text)['data']['token']
        else:
            # 序列化返回字典格式
            return json.loads(res.text)


if __name__ == '__main__':
    print(Login().login({"username":"","password":"xintian"},False))