# autu :liyongbing
# time: 2020/12/28
import pytest
import os


def get_data():
    return 1,2

@pytest.mark.parametrize('a,b,c',[(1,2,3)])
def test_add(a, b, c):
    assert a+b == c


def test_01():
    assert 1 == 1


@pytest.mark.parametrize('a', [1, 2, 4])
def test_add_cs(a):
    assert a == 4


@pytest.mark.parametrize('data', get_data())
def test_add_cs_2(a, b):
    assert a == b


@pytest.mark.parametrize('a,b,c',[(1,2,3),(2,3,4)])
def test_add_cs_3(a, b,c):
    assert a +b == c


if __name__ == '__main__':
    pytest.main(['test_base_pytest.py','-v', '-s','--alluredir' ,'../report/xml'])  # ../report/xml生成测试数据
    os.system('allure generate ../report/xml -o ../report/report/html --clean') # ./report/report/html目录生成测试数据 --clean 清除历史数据

