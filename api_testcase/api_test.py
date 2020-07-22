#!/usr/bin/env python
# encoding: utf-8
# @author: Alin
# @file: .py
# @time: 2020/7/22 9:34

import warnings
import unittest
import paramunittest
from common.request_utils import RequestsUtils
from common.testdata_utils import TestDataUtils

case_infos = TestDataUtils().get_test_case_data_list()


@paramunittest.parametrized(
    *case_infos
)
class APITest(paramunittest.ParametrizedTestCase):
    def setUp(self) -> None:
        warnings.simplefilter('ignore', ResourceWarning)

    def setParameters(self, case_id, case_info):
        self.case_id = case_id
        self.case_info = case_info

    def test_api_common_function(self):
        self._testMethodName = self.case_info[0].get('测试用例编号')
        self._testMethodDoc = self.case_info[0].get('测试用例名称')
        actual_result = RequestsUtils().request_by_step(self.case_info)
        self.assertTrue(actual_result.get('check_result'), actual_result.get('message'))


if __name__ == '__main__':
    unittest.main()
