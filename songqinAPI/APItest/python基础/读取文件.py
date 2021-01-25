# auto :liyongbing  
# time: 2020/12/23

import json



#
# with open('4.txt','r+', encoding='utf-8') as f, open('file.txt','r+',encoding='utf-8') as f1:
#     f.write('课程目标帮助手工测试工程师熟练掌握软件自动化测试技术，成长为一名出色的软件自动化测试工程师。通过Python编程、Web自动化、APP自动化、接口自动化、Robot Framework框架的学习与实战操作，帮助学员掌握软件自动化测试开发。熟练开展软件自动化测试工作。')
#     f.seek(0)
#     data = f.read()
#
#     print(data)
#     print(f1.readlines())


# 获取列表格式字符串
def readfile(file):
    with open(file,'r') as f:
        f.readline()
        data = f.read().splitlines()
        del data[-1]
    return data
# print(readfile('data.log'))
def tongji():
    json_data = 0
    jpep_data = 0
    png_data = 0
    other = 0
    for i in readfile('data.log'):
        tem = i.split('\t')
        # print(tem)
        daxiao = int(tem[1])
        geshi = tem[-2]
        if geshi =='image/jpeg':
            jpep_data += daxiao
        elif geshi == 'application/json':
            json_data += daxiao
        elif geshi == 'image/png':
            png_data += daxiao
        # print(daxiao,geshi)
        else:
            other += daxiao
            print('存在其他格式{},大小为：{}'.format(geshi, other,))

    print('json_data的大小:{},jpep_data的大小{}，png_data大小{}'.format(json_data, jpep_data, png_data))

tongji()