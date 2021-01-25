# -*- coding:utf-8 -*-
# autu :liyongbing  
# time: 2021/1/24

import yaml


def get_yaml_data(filedir):
    # 读取单个yaml文件
    # 加载ymal文件
    file = open(filedir, 'r', encoding='utf-8')
    res = yaml.load(file, Loader=yaml.FullLoader)

    return res


def get_yaml(filedir):
    # 处理用用例参数化格式--[(),()]
    data = []
    file = open(filedir, 'r', encoding='utf-8')
    res = yaml.load(file,Loader=yaml.FullLoader)
    # 返货数据样式--根据项目来
    del res[0]  # 删除第一个公告参数
    for i in res:
        data.append((i['data'],i['resp']))
    return data


def get_yaml_all(filedir):
    # 获取多个ymal文件
    date_list = []
    # 加载ymal文件
    file = open(filedir, 'r', encoding='gbk')
    res = yaml.load_all(file, Loader=yaml.FullLoader)
    for i in res:
        date_list.append(i)
    return (date_list)


if __name__ == '__main__':
    print(get_yaml('../data/login_case.yaml'))