#!/usr/bin/env python
# encoding: utf-8
# @author: Alin
# @file: .py
# @time: 2020/7/5 11:01

import os
from common.excel_utils import ExcelUtils
from common.local_config_utils import local_config

current_path = os.path.dirname(__file__)
test_data_path = os.path.join(current_path, '..', local_config.CASE_DATA_PATH)


class TestDataUtils():
    def __init__(self, data_path=test_data_path):
        self.data_path = data_path
        self.test_data = ExcelUtils(data_path, 'Sheet1').get_sheet_data_by_dict()

    def __get_test_case_data_dict(self):
        use_case_dict = {}
        for row_data in self.test_data:
            use_case_dict.setdefault(row_data['测试用例编号'], []).append(row_data)
        return use_case_dict

    def get_test_case_data_list(self):
        test_case_list = []
        for k, v in self.__get_test_case_data_dict().items():
            one_case_dict = {}
            one_case_dict["case_name"] = k
            one_case_dict['case_info'] = v
            test_case_list.append(one_case_dict)
        return test_case_list


if __name__ == '__main__':
    # a = ExcelUtils(test_data_path, 'Sheet1').get_sheet_data_by_dict()
    # print(a)
    testdataUtils = TestDataUtils()
    # for i in testdataUtils.__get_test_case_data_dict()['case01']:
    #     print(i)
    #
    print('-------------------------------------------------')
    for i in testdataUtils.get_test_case_data_list():
        print(i)
