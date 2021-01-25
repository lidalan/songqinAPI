# autu :liyongbing
# time: 2021/1/2
import requests
import json
HOST = 'http://127.0.0.1:8111'
# url = f'{HOST}//api/mgr/loginReq'


def login(username, pwd, flag=True):
    url = f'{HOST}/api/mgr/loginReq'
    payload = {'username': username,
            'password': pwd}
    headers = {'Content-Type': 'application/x-www-form-urlencoded'}
    res = requests.post(url=url, data=payload, headers=headers)
    if flag:
        # 第一种直接获取cookies
        # return res.cookies
        # print(res.cookies)
        # 第二种，后续需要动态拼接
        return res.cookies['sessionid']
    else:
        # print(res.text)
        # print(res.json())
        print(json.loads(str(res.text)))
        # print(res.request.body)
        # print(res.request.headers)
        # print(res.headers)


# print(res.headers)

if __name__ == '__main__':

    login('auto','sdfsdfsdf',flag=False)
