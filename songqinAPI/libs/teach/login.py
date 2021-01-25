# -*- coding:utf-8 -*-
# autu :liyongbing  
# time: 2021/1/16
import requests


Host = 'http://localhost:8111'


class Login:
    def login(self, inDate,getCookies=False):
        payload =inDate
        url = f'{Host}/api/mgr/loginReq'
        res = requests.post(url=url, data=payload)
        if getCookies:
            print(res.json())

        else:
            print(res.cookies['sessionid'])
            print(res.request._cookies)


if __name__ == '__main__':
    Login().login({'username': 'auto', 'password': 'sdfsdfsdf'})