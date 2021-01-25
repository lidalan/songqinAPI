# autu :liyongbing
# time: 2020/12/29

from APItest.teach.day_02_cookies_login import login
import json
import requests

# 主机名
HOST = 'http://127.0.0.1:8111'
def add_course1():
    url = f'{HOST}/api/mgr/sq_mgr/'
    header = {'Content-Type':'application/x-www-form-urlencoded'}
    # header = {'Content-Type':'application/x-www-form-urlencoded'}
    # 参数
    payload = {
        "action": 'add_course',
        "data": '''{
                "name":"几何",
                "desc":"初中几何课程1",
                "display_idx":"5"}'''
    }
    res = requests.post(url=url, data=payload, headers=header)
    # print(json.loads(str(res.text)))
    # print(res.text)
    # res.encoding = 'unicode_escape'
    # print(res.text)
    print(json.loads(str(res.text)))
    # print(res.json())
    #
    # print(res.request.headers)# 查看请求头
    # print(res.request.url)
    # print(res.request.body)
    # print(res.url)
    # print(res.headers)   # 查看响应头

    # print(res.cookies)


def add_course():
    url = f'{HOST}/api/mgr/sq_mgr/'
    header = {'Content-Type': 'application/x-www-form-urlencoded'}
    # 第一种场景：直接获取cookies
    # cookie = login('auto','sdfsdfsdf')
    # 第二种场景 动态拼接  sessionid关键字不能写错----自己封装
    user_sessionid = login('auto','sdfsdfsdf')
    cookie = {'sessionid':user_sessionid}

    # header = {'Content-Type':'application/x-www-form-urlencoded'}
    # 参数
    payload = {
        "action": 'add_course',
        "data": '''{
                "name":"几何",
                "desc":"初中几何课程1",
                "display_idx":"5"}'''
    }
    res = requests.post(url=url, data=payload, headers=header, cookies=cookie)
    print(json.loads(str(res.text)))
    # print(res.headers)
    # print(res.request.headers)


if __name__ == '__main__':
    add_course()
