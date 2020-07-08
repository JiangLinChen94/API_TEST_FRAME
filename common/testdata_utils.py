#!/usr/bin/env python
# encoding: utf-8
# @author: Alin
# @file: .py
# @time: 2020/7/5 11:01

import os
from common.excel_utils import ExcelUtils
from common import config

current_path = os.path.dirname(__file__)
test_data_path = os.path.join(current_path, '..', r'test_data\test_case.xlsx')

class TestdataUtils():
    def __init__(self, data_path=test_data_path):
        self.data_path = data_path
        self.test_data = ExcelUtils(data_path, 'Sheet1').get_sheet_data_by_dict()

    def get_testcase_data(self):
        testcase_dict = {}
        for row_data in self.test_data:
            testcase_dict.setdefault(row_data['测试用例编号'], []).append(row_data)
        return testcase_dict

    def get_testcase_data_list(self):
        testcase_list = []
        for k,v in self.get_testcase_data().items():
            one_case_dict = {}
            one_case_dict["case_name"] = k
            one_case_dict['case_info'] = v
            testcase_list.append(one_case_dict)
        return testcase_list


if __name__ == '__main__':
    # a = ExcelUtils(test_data_path, 'Sheet1').get_sheet_data_by_dict()
    # print(a)
    testdataUtils = TestdataUtils()
    for i in testdataUtils.get_testcase_data()['case01']:
        print(i)
    #
    # for i in testdataUtils.get_testcase_data_list():
    #     print(i)