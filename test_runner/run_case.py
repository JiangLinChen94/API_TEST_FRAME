#!/usr/bin/env python
# encoding: utf-8
# @author: Alin
# @file: .py
# @time: 2020/7/23 17:25

import os
import unittest
from common.local_config_utils import local_config
from common import HTMLTestReportCN

current_path = os.path.dirname(__file__)
test_case_path = os.path.join(current_path, '..', local_config.CASE_PATH)
test_report_path = os.path.join(current_path, '..', local_config.REPORTS_PATH)


class RunCase:
    def __init__(self):
        self.case_path = test_case_path
        self.report_path = test_report_path
        self.title = 'VXAPI接口自动化报告'
        self.description = '自动化接口框架学习专用'
        self.tester = '我们'

    def load_test_suit(self):
        discover = unittest.defaultTestLoader.discover(start_dir=self.case_path,
                                                       pattern='api_test.py',
                                                       top_level_dir=self.case_path)
        all_suite = unittest.TestSuite()
        all_suite.addTest(discover)
        return all_suite

    def run(self):
        report_dir = HTMLTestReportCN.ReportDirectory(self.report_path)
        report_dir.create_dir(self.title)
        report_file_path = HTMLTestReportCN.GlobalMsg.get_value('report_path')
        fp = open(report_file_path, 'wb')
        runner = HTMLTestReportCN.HTMLTestRunner(stream=fp,
                                                 title=self.title,
                                                 description=self.description,
                                                 tester=self.tester)
        runner.run(self.load_test_suit())
        fp.close()
        return report_file_path


if __name__ == '__main__':
    report_path = RunCase().run()
