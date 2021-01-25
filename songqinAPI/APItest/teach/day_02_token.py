# auto :liyongbing  
# time: 2021/1/2
import requests
import json


def get_token():
    # 登录-获取token
    url = 'http://47.96.181.17:9090/rest/toController'
    data = {'userName': 'J201903070064',
            'password': '362387359'}
    header = {'Content-Type': 'application/json'}
    res = requests.post(url=url, json=data, headers=header)
    # 转化成字典，获取token键值
    return json.loads(res.text)['token']
    # return res.text['token']


def add_user():
    url = 'http://47.96.181.17:9090/rest/ac01CrmController'
    data = {
        'acc003': 'lidada',
        'acc004': '1',
        'acc011': '21',
        'acc030': '15251522635',
        'acc01u': '88002255',
        'crm003': '1',
        'crm004': '1',
        'crm00a': '2020-12-12',
        'crm00b': 'aaaa',
        'crm00c': '2020-12-25',
        'crm00d': 'bbbbb'}
    header = {'Content-Type': 'application/json',
              'X-AUTH-TOKEN': get_token()}
    res = requests.post(url=url, json=data, headers=header)
    print(res.request.headers)
    print(res.text)

if __name__ == '__main__':
    print(get_token())
    add_user()