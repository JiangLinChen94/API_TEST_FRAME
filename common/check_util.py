#!/usr/bin/env python
# encoding: utf-8
# @author: Alin
# @file: .py
# @time: 2020/7/19 21:19
import ast
import re


class CheckUtil():
    def __init__(self, check_response=None):
        self.check_response = check_response
        self.check_rules = {
            '无': self.no_check,
            'json键是否存在': self.check_key,
            'json键值对': self.check_keyValue,
            '正则匹配': self.check_regexp
        }
        self.pass_result = {
            'code': 0,
            'response_reason': self.check_response.reason,
            'response_code': self.check_response.status_code,
            'response_headers': self.check_response.headers,
            'response_body': self.check_response.text,
            'check_result': True,
            'message': ''  # 扩展作为日志输出等
        }
        self.fail_result = {
            'code': 2,
            'response_reason': self.check_response.reason,
            'response_code': self.check_response.status_code,
            'response_headers': self.check_response.headers,
            'response_body': self.check_response.text,
            'check_result': False,
            'message': ''  # 扩展作为日志输出等
        }

    def no_check(self):
        return self.pass_result

    def check_key(self, check_data=None):
        check_data_list = check_data.split(',')
        res_list = []  # 存放每次比较的结果
        wrong_key = []  # 存放比较失败的key
        for check_data in check_data_list:
            if check_data in self.check_response.json().keys():
                res_list.append(self.pass_result)
            else:
                res_list.append(self.fail_result)
                wrong_key.append(check_data)
        if self.fail_result in res_list:
            return self.fail_result
        else:
            return self.pass_result

    def check_keyValue(self, check_data=None):
        res_list = []
        wrong_items = []
        for check_item in ast.literal_eval(check_data).items():
            if check_item in self.check_response.json().items():
                res_list.append(self.pass_result)
            else:
                res_list.append(self.fail_result)
                wrong_items.append(check_item)
        if self.fail_result in res_list:
            return self.fail_result
        else:
            return self.pass_result

    def check_regexp(self, check_data=None):
        pattern = re.compile(check_data)
        if re.findall(pattern=pattern, string=self.check_response.text):
            # print(self.pass_result)
            return self.pass_result
        else:
            return self.fail_result

    def run_check(self, check_type=None, check_data=None):
        code = self.check_response.status_code
        if code == 200:
            if check_type in self.check_rules.keys():
                result = self.check_rules[check_type](check_data)
                return result
            else:
                self.fail_result['message'] = '不支持%s判断方法' % check_type
                return self.fail_result
        else:
            self.fail_result['message'] = '请求状态码%s,非200' % str(code)
            return self.fail_result


if __name__ == '__main__':
    # CheckUtil().check_key("access_token,expires_in")
    pass