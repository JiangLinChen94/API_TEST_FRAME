#!/usr/bin/env python
# encoding: utf-8
# @author: Alin
# @file: .py
# @time: 2020/7/5 8:58
import os
import xlrd


class ExcelUtils():
    def __init__(self, file_path, sheet_name):
        self.file_path = file_path
        self.sheet_name = sheet_name
        self.sheet = self.get_sheet()

    def get_sheet(self):
        wookbook = xlrd.open_workbook(self.file_path)
        sheet = wookbook.sheet_by_name(self.sheet_name)
        return sheet

    def get_row_count(self):
        row_count = self.sheet.nrows
        return row_count

    def get_col_count(self):
        col_count = self.sheet.ncols
        return col_count

    def __get_cell_value(self, row_index, col_index):
        cell_value = self.sheet.cell_value(row_index, col_index)
        return cell_value

    def get_merged_info(self):
        merged_info = self.sheet.merged_cells
        return merged_info

    def get_merged_cell_value(self, row_index, col_index):
        for merged in self.get_merged_info():
            if (row_index >= merged[0] and row_index < merged[1] and col_index >= merged[2] and col_index < merged[3]):
                return self.__get_cell_value(merged[0], merged[2])
        return self.__get_cell_value(row_index, col_index)

    def get_sheet_data_by_dict(self):
        all_data_list = []
        first_row = self.sheet.row(0)
        for row in range(1, self.get_row_count()):
            row_dict = {}
            for col in range(0, self.get_col_count()):
                row_dict[first_row[col].value] = self.get_merged_cell_value(row, col)
            all_data_list.append(row_dict)
        return all_data_list


if __name__ == '__main__':
    current_path = os.path.dirname(__file__)
    excel_path = os.path.join(current_path, r'..\test_data\test_case.xlsx')
    excelUtils = ExcelUtils(excel_path, 'Sheet1')
    # value = excelUtils.get_merged_cell_value(8, 0)
    # print(value)
    for data in excelUtils.get_sheet_data_by_dict():
        print(data)
    # print(excelUtils.get_sheet_data_by_dict())

