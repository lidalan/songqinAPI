# -*- coding:utf-8 -*-
# autu :liyongbing  
# time: 2021/1/21
import pytest
from tools.read_excel import ReadExcel
from libs.login import Login
from libs.shop import Shop
from libs.food import Food
from tools.file_upload import file_upload
from config.config import filename, filepath, filetype,HOST
import os
import allure


# {'code': 20000, 'data': '', 'flag': '松勤教育', 'msg': '成功', 'success': False}

@allure.epic('外卖项目')
@allure.feature('食品模块')
class Test_food:

    @pytest.mark.parametrize('inData', ReadExcel().get_datas('食品管理', 'AddfoodkindByErrorid'))
    @allure.description('店铺错误存在')
    @allure.story('新增商铺类型_商铺id错误')
    @allure.title('错误商铺id')
    def test_add_food_error_id(self, inData, food):
        # 前置商铺id
        # print(type(inData[1]))
        # inData[0]['restaurant_id'] = shop_init[0]
        # 发送添加食品请求
        res = food.add_food_type(inData[0])

        if 'code' in res:
            assert res['code'] == inData[1]['code']
        else:
            assert res['error'] == inData[1]['error']

    @allure.description('店铺id正确')
    @allure.story('新增商铺类型_商铺id正确')
    @allure.title('商铺店铺id正确')
    @pytest.mark.parametrize('inData', ReadExcel().get_datas('食品管理', 'AddfoodkindByRightid'))
    def test_add_food_right_id(self,inData, food, shop_init):
        inData[0]['restaurant_id'] = shop_init[0]
        res = food.add_food_type(inData[0])
        if 'code' in res:
            assert res['code'] == inData[1]['code']
        else:
            assert res['error'] == inData[1]['error']
        pass

if __name__ == '__main__':
    try:
        for i in os.listdir('../report/tmp/'):
            if 'json'in i or 'txt' in i:
                os.remove(f'../report/tmp/{i}')

    except:
        print('初次运行，暂时无数据')
    pytest.main(['-v', '-s', 'test_food.py', '--alluredir=../report/tmp'])
    os.system('allure generate ../report/tmp -o ../report/html --clean')
    #
