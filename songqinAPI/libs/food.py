# -*- coding:utf-8 -*-
# autu :liyongbing  
# time: 2021/1/21
from libs.login import Login
import pprint
import requests
import json
from config.config import HOST
fiddler = {'http': 'http://127.0.0.1:8888'}


class Food:
    def __init__(self, token):
        self.token = token

    def add_food_type(self, in_data):
        url = f'{HOST}/shopping/addcategory'
        header = {'Authorization': self.token
                  }
        payload = in_data
        res = requests.post(url=url, data=payload, headers=header)
        # res = requests.post(url=url, data=payload, headers=header, proxies=fiddler)
        return res.json()

    def add_food(self, in_data):
        url = f'{HOST}/shopping/addcategory'
        header = {'Authorization': self.token}
        payload = in_data
        res = requests.post(url=url, data=payload, headers=header)
        # res = requests.post(url=url, data=payload, headers=header, proxies=fiddler)
        return res.json()

    def get_food_type(self, category_id,get_id=True):
        url = f'{HOST}/shopping/getcategory/{category_id}'
        res = requests.get(url=url)
        food_typeId = []
        if get_id:
            # print(json.loads(res.text)['category_list'])  # 83
            for i in json.loads(res.text)['category_list']:
                if 'name' in i:
                    # print(i['name'])
                    food_typeId.append((int(i['id']),i['name']))
                    id = i["id"]
                    with open('../data/food_typeId.txt', 'a', encoding='utf-8') as f:
                        f.write(f'{id}\r')
            print(food_typeId)
            return food_typeId
        # else:
            print(json.loads(res.text))

    def food_add(self,inDate):
        url =f'{HOST}/shopping/addmyfood'
        payload = inDate
        header = {'Authorization': self.token}
        res = requests.post(url=url,data=payload,headers=header)
        print(res.json())


if __name__ == '__main__':

    token = Login().login({'username': 'md0083', 'password': 37924})
    food = Food(token)
    # print(Shop(token).shop_list({'page': -1, 'limit': 20}))
#     data ={'restaurant_id':"9999999999",
# 'name':'牛奶111',
# 'description':'旺仔牛奶'}
#     print(Food(token).add_food_type(data))
    da = {'name':'乡里鸡腿堡11',
'descript':'很好好持有',
'idShop':'7715',
'category_id':'10390',
'image_path':'1596e89a-75b4-483b-9415-5aba8bc6f2aa.jpg',
'activity':'满5减1',
'attributesJson':'["新"]',
'specsJson':'[{"specs":"默认","packing_fee":1,"price":20}]'}
    food.food_add(da)
