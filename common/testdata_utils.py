#!/usr/bin/env python
# encoding: utf-8
# @author: Alin
# @file: .py
# @time: 2020/7/5 11:01

import os
import pandas as pd
from common.excel_utils import ExcelUtils
from common.local_config_utils import local_config
from common.sql_utils import SqlUtils

current_path = os.path.dirname(__file__)
test_data_path = os.path.join(current_path, '..', local_config.CASE_DATA_PATH)


class TestDataUtils():
    def __init__(self, data_path=test_data_path):
        """
        :param data_path:excel数据存放路径
        """
        self.data_path = data_path
        self.test_data_sheet = ExcelUtils(data_path, 'Sheet1')
        self.test_data = self.test_data_sheet.get_sheet_data_by_dict()
        self.test_data_by_mysql = SqlUtils().get_mysql_test_case_info()

    def __get_test_case_data_dict(self):
        '''
        :return: 返回字典格式数据
        '''
        use_case_dict = {}
        for row_data in self.test_data:
            if row_data['用例执行'] == '是':
                use_case_dict.setdefault(row_data['测试用例编号'], []).append(row_data)
        return use_case_dict

    def get_test_case_data_list(self):
        """
        :return: 封装成字典格式case_id为key，case_info为value
        """
        test_case_list = []
        for k, v in self.__get_test_case_data_dict().items():
            one_case_dict = {}
            one_case_dict["case_id"] = k
            one_case_dict['case_info'] = v
            test_case_list.append(one_case_dict)
        return tuple(test_case_list)

    def __get_test_case_data_dict_by_mysql(self):
        use_case_dict = {}
        for row_data in self.test_data_by_mysql:
            use_case_dict.setdefault(row_data['测试用例编号'], []).append(row_data)
        return use_case_dict

    def get_test_case_data_list_by_mysql(self):
        test_case_list = []
        for k, v in self.__get_test_case_data_dict_by_mysql().items():
            one_case_dict = {}
            one_case_dict["case_id"] = k
            one_case_dict['case_info'] = v
            test_case_list.append(one_case_dict)
        return tuple(test_case_list)

    def get_row_num(self, case_id, case_step_name):
        for j in range(len(self.test_data)):
            if self.test_data[j]['测试用例编号'] == case_id and self.test_data[j]['测试用例步骤'] == case_step_name:
                break
        return j + 1

    def get_result_index(self):
        for col_index in range(len(self.test_data_sheet.sheet.row(0))):
            if self.test_data_sheet.sheet.row(0)[col_index].value == '测试结果':
                break
        return int(col_index)

    def write_result_to_excel(self, case_id, case_step_name, content='通过'):
        row_index = self.get_row_num(case_id, case_step_name)
        col_index = self.get_result_index()
        self.test_data_sheet.update_excel_data(row_index, col_index, content)

    def clear_result_from_excel(self):
        row_count = self.test_data_sheet.get_row_count()
        col_index = self.get_result_index()
        self.test_data_sheet.clear_excel_column(1, row_count, col_index)


if __name__ == '__main__':
    # a = ExcelUtils(test_data_path, 'Sheet1').get_sheet_data_by_dict()
    # print(a)
    testdataUtils = TestDataUtils()
    # for i in testdataUtils.get_test_case_data_list():
    #     print(i)update_excel_data
    testdataUtils.get_result_index()
    print(type(testdataUtils.get_result_index()))