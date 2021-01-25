# -*- coding:utf-8 -*-
# autu :liyongbing  
# time: 2021/1/18
import pytest
from libs.login import Login
from libs.shop import Shop
from tools.file_upload import file_upload
from config.config import filename, filepath, filetype,HOST,login_data
import os
from libs.food import Food


@pytest.fixture(autouse=True)
def start():
    print('\n-------------测试开始------------')
    yield
    print('\n-----------用例执行结束-----------')


# 初始化登录
@pytest.fixture(scope='session')
def login_init():
    token = Login().login(login_data)
    print('\n---------登录初始化---------')
    return token


# 商铺实例化对象初始化
@pytest.fixture(scope='class')
def shop(login_init):
    shop = Shop(login_init)
    print('\n---------商铺初始化---------')
    return shop

# 食品实例化对象初始化
@pytest.fixture(scope='class')
def food(login_init):
    foods = Food(login_init)
    print('\n---------商铺初始化---------')
    return foods


# 食品类型id--默认获取第一个
@pytest.fixture(scope='class')
def food(foods, shop_init):
    food_type_id = foods.get_food_type(shop_init[0])
    return food_type_id[0][0]

# 商铺修改前置初始化
@pytest.fixture(scope='function')
def shop_init(login_init, shop):

    id = shop.shop_list({'page': 5, 'limit': 20})
    photo = file_upload(filename, filepath, filetype, login_init)
    print('\n---------商铺前置初始化---------')
    # print(id, photo)
    return id, photo
