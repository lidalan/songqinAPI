# -*- coding:utf-8 -*-
# autu :liyongbing  
# time: 2021/1/21

import json,requests,pprint

url = 'http://121.41.14.39:8082/shopping/getcategory/7715'
res = requests.get(url)
a = ((json.loads(res.text)['category_list']))
b=[]
for i in a:
    b.append(int(i['id']))
# a = [0]['foods'][0]['id']
pprint.pprint(b)

for i in b:
    url1 =f'http://121.41.14.39:8082/shopping/v2/fooddel/{i}'
# url1 =/shopping/v2/fooddel/{id}

res = requests.post(url1)
print(res)
