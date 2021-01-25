# -*- coding:utf-8 -*-
# autu :liyongbing  
# time: 2021/1/13

from libs.login import Login
import pprint,json
import requests
from config.config import HOST
fiddler = {'http': 'http://127.0.0.1:8888'}


class Shop:

    # 初始化店铺实例，只需要鉴权一次
    def __init__(self, inToken):
        self.token = inToken

    # 查看获取店铺列表信息
    def shop_list(self, inDate, getId=False):
        """:arg
            inDate :输入参数
            getId=True 获取店铺信息  False：获取店铺id

        """
        url = f'{HOST}/shopping/myShop'
        payload = inDate
        header = {'content-type': 'application/json',
                  'Authorization': self.token}
        # res = requests.get(url=url, headers=header, data=payload, proxies=fiddler)
        res = requests.get(url=url, headers=header, json=payload)
        if getId:
            return res.json()
        else:
            return res.json()['data']['records'][0]['id']

    def shop_updata(self, inData):
        url = f'{HOST}/shopping/updatemyshop'
        payload =inData
        header = {'Authorization': self.token}
        res = requests.post(url=url, headers=header, data=payload)

        return res.json()['code']


if __name__ == '__main__':
    # addcategory({'name': '小吃7', 'description': '好哈', 'restaurant_id': 7715})
    token = Login().login({'username': 'md0083', 'password': 37924})
    # print(Shop(token).shop_list({"page":1,"limit":-1},True))
    # Shop(token).shop_updata()
    #
    # url = 'http://121.41.14.39:8082/shopping/getcategory/7715'
    # res = requests.get(url)
    # a = ((json.loads(res.text)['category_list']))
    # b = []
    # for i in a:
    #     b.append(int(i['id']))
    # # a = [0]['foods'][0]['id']
    # # pprint.pprint(b)
    #
    # for i in b:
    #     pass
    url1 = f'http://121.41.14.39:8082/shopping/v2/fooddel/10390'
    # url1 =/shopping/v2/fooddel/{id}
    header = {'Authorization':token}
    data ={"id":10390}
    res = requests.delete(url1,headers=header,data=data)
    print(res.json())