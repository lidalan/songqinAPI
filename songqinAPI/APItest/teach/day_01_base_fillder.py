# autu :liyongbing
# time: 2020/12/29


import json
import requests

filder_proxies ={'http':'http://127.0.0.1:8888'}
# 主机名
host = 'http://127.0.0.1:8111'
url = f'{host}/api/mgr/sq_mgr/'
header = {'Content-Type':'application/x-www-form-urlencoded'}

# 参数
payload = {
    "action": 'add_course',
    "data": '''{
            "name":"几何",
            "desc":"初中几何课程",
            "display_idx":"4"}'''
}
res = requests.post(url=url, data=payload, headers=header,proxies=filder_proxies)
print(json.loads(str(res.text)))

