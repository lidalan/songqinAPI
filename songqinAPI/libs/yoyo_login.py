# -*- coding:utf-8 -*-
# autu :liyongbing  
# time: 2021/1/20
import requests


url = 'http://49.235.92.12:8020/xadmin/hello/teacherman/'
res = requests.get(url)
print(res)