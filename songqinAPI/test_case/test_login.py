# -*- coding:utf-8 -*-
# autu :liyongbing  
# time: 2021/1/17
from libs.login import Login
from tools.read_excel import ReadExcel
from config.config import excel_path
import pytest,allure,os


@allure.epic('外卖项目')
@allure.feature('登录模块')
class TestLogin:

    @pytest.mark.parametrize('indata',ReadExcel().get_datas('登录模块','Login'))
    @allure.story('登录模块测试')
    @allure.title('登录用例')
    def test_login(self,indata):
        res = Login().login(indata[0], False)
        # print(res)
        assert res['msg'] == indata[1]['msg']
if __name__ == '__main__':


    try:
        for i in os.listdir('../report/tmp/'):
            if 'json'in i or 'txt' in i:
                os.remove(f'../report/tmp/{i}')

    except:
        print('初次运行，暂时无数据')
    pytest.main(['-v', '-s', 'test_login.py', '--alluredir=../report/tmp'])
    os.system('allure generate ../report/tmp -o ../report/html --clean')