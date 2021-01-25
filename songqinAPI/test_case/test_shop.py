# -*- coding:utf-8 -*-
# autu :liyongbing  
# time: 2021/1/18
import pytest
from tools.read_excel import ReadExcel
from libs.login import Login
from libs.shop import Shop
from tools.file_upload import file_upload
from config.config import filename, filepath, filetype,HOST
import os
import allure


@allure.epic('外卖项目')
@allure.feature('商铺模块')
@pytest.mark.shop
class TestShop:

    @allure.description('前置条件，商店存在用例')
    @allure.story('商铺修改')
    @allure.title('商铺修改用例')
    @pytest.mark.shop_update
    # @pytest.mark.skip
    @pytest.mark.parametrize('in_data', ReadExcel().get_datas('我的商铺', 'updateshopping'))
    def test_shop_update(self, shop, in_data, shop_init):
        # 修改图片字段信息
        in_data[0]['image_path'] = shop_init[1]
        in_data[0]['image'] = f"{HOST}/file/getImgStream?fileName={shop_init[1]}"
        # 修改id
        in_data[0]['id'] = shop_init[0]
        # 店铺更新
        res = shop.shop_updata(in_data[0])
        assert res == in_data[1]['code']

    @allure.description('前置条件，商店存在用例')
    @allure.story('商铺列表')
    @pytest.mark.shop_update
    @pytest.mark.parametrize('in_data', ReadExcel().get_datas('我的商铺', 'listshopping'))
    @allure.title('{in_data[0]}')
    def test_shop_list(self, shop, in_data):

        res = shop.shop_list(in_data[0], True)
        if 'code' in res:
            assert res['code'] == in_data[1]['code']
        else:
            assert res['error'] == in_data[1]['error']

if __name__ == '__main__':
    try:
        for i in os.listdir('../report/tmp/'):
            if 'json'in i or 'txt' in i:
                os.remove(f'../report/tmp/{i}')

    except:
        print('初次运行，暂时无数据')
    pytest.main(['-v', '-s', 'test_shop.py::TestShop::test_shop_list', '--alluredir=../report/tmp'])
    os.system('allure generate ../report/tmp -o ../report/html --clean')
    #




