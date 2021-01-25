# -*- coding:utf-8 -*-
# auto :liyongbing
# time: 2021/1/5
from APItest.teach.test_emis_course import Test_Emis
import xlrd
import json
from xlutils.copy import copy


filename =r'C:\Users\51064\Desktop\松勤-教管系统接口测试用例-v1.4.xls'

workBook = xlrd.open_workbook(filename=filename,formatting_info=True)
# formatting_info=True 原样打开文件，xlsx格式无法设置
sheet_names = workBook.sheet_names()  # 查看所有表名，列表展示
# print(sheet_names)

# 打开表格
# 通过下标
# work_sheet = workBook.sheet_by_index(1)
# 通过表面
work_sheet = workBook.sheet_by_name('1-登录接口')

# 下标从0开始
# 获取列数据，返回列表
col_datas = work_sheet.col_values(0)
# print(col_datas)

# 获取行数据，返回列表
row_datas = work_sheet.row_values(0)
# print(row_datas)

# 获取列长度
cols = work_sheet.ncols
print(cols)

# 获取 行长度
rows = work_sheet.nrows
print(rows)

# 获取单元格数据，返回字符串
def get_cell(col, row=6):
    cell_data = work_sheet.cell_value(col, row)
    # print(cell_data)
    data = json.loads(cell_data)
    return data

# 在缓存中copy一个新的excel
new_book = copy(workBook)
# 取表
new_sheet = new_book.get_sheet(1)

res = Test_Emis().test_login(get_cell(1)['username'], get_cell(1)['password'], flag=False)
if res['retcode'] == 0:
    info = 'Pass'
    new_sheet.write(1,9,info)
    print('--------Pass---------')
else:
    info = 'Fail'
    new_sheet.write(2, 9, info)
    print('--------fail---------')



# 保存新表
new_book.save('./new_excel.xls')
# if __name__ == '__main__':
#
#     res = Test_Emis().test_login(get_cell(2)['username'], get_cell(2)['password'], flag=False)
#     if res['retcode'] == 0:
#         print('Pass')
#     else:
#         print('fail')
#     # print((res))