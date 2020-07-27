#!/usr/bin/env python
# encoding: utf-8
# @author: Alin
# @file: .py
# @time: 2020/7/5 8:58
import os
import xlrd
from xlutils.copy import copy


class ExcelUtils:
    def __init__(self, file_path, sheet_name):
        '''
        :param file_path: 文件路径
        :param sheet_name: 文件标签名称
        '''
        self.file_path = file_path
        self.wb = xlrd.open_workbook(self.file_path, formatting_info=True)
        self.sheet_name = sheet_name
        self.sheet = self.get_sheet()

    def get_sheet(self):
        '''
        :return:将文本打开后，将相应方法传个sheet并返回
        '''
        sheet = self.wb.sheet_by_name(self.sheet_name)
        return sheet

    def get_row_count(self):
        '''
        :return: 返回行数
        '''
        row_count = self.sheet.nrows
        return row_count

    def get_col_count(self):
        '''
        :return: 返回列数
        '''
        col_count = self.sheet.ncols
        return col_count

    def __get_cell_value(self, row_index, col_index):
        """
        读取相应单元格中内容
        :param row_index: 行号
        :param col_index: 列号
        :return:
        """
        cell_value = self.sheet.cell_value(row_index, col_index)
        return cell_value

    def get_merged_info(self):
        """
        :return:返回的是一个列表，每一个元素是合并单元格的位置信息的数组，数组包含四个元素（起始行，结束行，起始列，结束列）
        """
        merged_info = self.sheet.merged_cells
        return merged_info

    def get_merged_cell_value(self, row_index, col_index):
        """
        读取合并单元格、或普通单元格内的cell
        :param row_index:行号
        :param col_index:列号
        :return:
        """
        for merged in self.get_merged_info():
            if (row_index >= merged[0] and row_index < merged[1] and col_index >= merged[2] and col_index < merged[3]):
                return self.__get_cell_value(merged[0], merged[2])
        return self.__get_cell_value(row_index, col_index)

    def get_sheet_data_by_dict(self):
        """
        :return:将所有数据已字典格式返回
        """
        all_data_list = []
        first_row = self.sheet.row(0)
        for row in range(1, self.get_row_count()):
            row_dict = {}
            for col in range(0, self.get_col_count()):
                row_dict[first_row[col].value] = self.get_merged_cell_value(row, col)
            all_data_list.append(row_dict)
        return all_data_list

    def update_excel_data(self, row_index, col_index, content):
        new_wb = copy(self.wb)
        sheet = new_wb.get_sheet(self.wb.sheet_names().index(self.sheet_name))
        sheet.write(row_index, col_index, content)
        new_wb.save(self.file_path)

    def clear_excel_column(self, start_index, end_index, col_index):
        new_wb = copy(self.wb)
        sheet = new_wb.get_sheet(self.wb.sheet_names().index(self.sheet_name))
        for row_index in range(start_index, end_index):
            sheet.write(row_index, col_index, '')
        new_wb.save(self.file_path)


if __name__ == '__main__':
    current_path = os.path.dirname(__file__)
    excel_path = os.path.join(current_path, r'..\test_data\test_case.xls')
    excelUtils = ExcelUtils(excel_path, 'Sheet1')
    print(excelUtils.get_col_count()['测试结果'].index())
    # excelUtils.update_excel_data(3, 14, '通过')
    # value = excelUtils.get_merged_cell_value(8, 0)
    # print(value)
    # for data in excelUtils.get_sheet_data_by_dict():
    #     print(data)
    # print(excelUtils.get_sheet_data_by_dict())
