# -*- coding:utf-8 -*-
# autu :liyongbing  
# time: 2021/1/16
import xlrd
from config.config import excel_path,run_excel_path
from xlutils.copy import copy
import traceback
import json


class ReadExcel:
    # formatting_info = True  xls格式使用
    def __init__(self):
        self.table = xlrd.open_workbook(excel_path, formatting_info=True)
        self.new_table = copy(self.table)  # 拷贝一个新表

    def get_sheet(self, sheetName):
        try:
            # 打开excel文件，formatting_info=True--保持原样式

            sheet = self.table.sheet_by_name(sheetName)

            return sheet
        except Exception as e:
            print(f'文件读取错误：{e}')

    def get_datas(self, sheetName, caseName, flag=0, dataNum=9):
        """获取用例数据"""
        resList = []
        try:
            # 变量接收一下表格对象
            sheet = self.get_sheet(sheetName)
            index = 0  # 遍历下标
            # 获取用例标题所在的列数据
            for datas in sheet.col_values(flag):
                # 如果用例模块在获取的datas范围内
                if caseName in datas:
                    # 请求参数和预期结果所在的列需要修改，则需要改变关系
                    res_body = sheet.cell_value(index, dataNum)  # 请求参数
                    res_expect = sheet.cell_value(index, dataNum+2)
                    # print(type(res_body),type(res_expect))# 预期结果
                    # 存储数据--list
                    # 处理接口请求参数-----dict格式
                    resList.append((json.loads(res_body), json.loads(res_expect)))
                    # print(resList)
                index += 1

            return resList
        except Exception as e:
            print(f'获取数据错误：{e}',traceback.format_exc())

    # def get_datas(self, sheetName,caseName):
    #     """获取用例数据"""
    #     resList =[]
    #     try:
    #         # 打开excel文件，formatting_info=True--保持原样式
    #         table = xlrd.open_workbook(self.excelPath, formatting_info=True)
    #         sheet = table.sheet_by_name(sheetName)
    #         # 获取所有表名
    #         names = table.sheet_names()
    #         # print(names)
    #         # 获取一行数据
    #         # print(sheet.row_values(2))
    #         # 获取列数据
    #         # print(sheet.col_values(9))
    #         # 获取单元格数据
    #         # print(sheet.cell_value(3,9))
    #         # print(sheet.cell(3, 9).value)
    #         # 遍历第0列--匹配
    #         insex = 0# 遍历下标
    #         for i in sheet.col_values(0):
    #             if caseName in i:
    #                 resbody = sheet.cell_value(insex, 9)
    #                 res_expect = sheet.cell_value(insex, 11)
    #                 # 存储数据--list
    #                 # 处理接口请求参数-----dict格式
    #                 resList.append((json.loads(resbody), json.loads(res_expect)))
    #
    #             insex+=1
    #         # pprint.pprint(resList)
    #         return resList
    # xlrd 单元格从0开始
    # 获取单元格数据 --for 读取测试用例---缺点存在异常数据或修改数据后可能读取会出现错误
    # 获取行数据
    # 获取列数据
    # 写数据
    def write_excel(self, index, col ,row, txt,filename=run_excel_path):
        new_sheet = self.new_table.get_sheet(index)
        new_sheet.write(col, row, txt)
        self.new_table.save(filename)
        # print(new_sheet)
if __name__ == '__main__':
    ex = ReadExcel()
    print((ex.get_datas('食品管理','AddfoodkindByErrorid')))
    # ex.write_excel(0,1,12,'pass')
    # ex.write_excel(0, 2, 12, 'fail')




