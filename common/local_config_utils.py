#!/usr/bin/env python
# encoding: utf-8
# @author: Alin
# @file: .py
# @time: 2020/7/11 11:04

import os
import configparser

current_path = os.path.dirname(__file__)
config_path = os.path.join(current_path, '..', r'conf/config.ini')


class LocalConfigUtils():
    def __init__(self, config_path=config_path):
        self.cfg = configparser.ConfigParser()
        self.cfg.read(config_path, encoding='utf-8')

    @property  # 把方法变为属性方法
    def URL(self):
        url_value = self.cfg.get('default', 'URL')
        return url_value

    @property
    def CASE_DATA_PATH(self):
        case_data_path = self.cfg.get('path', 'CASE_DATA_PATH')
        return case_data_path

    @property
    def LOG_PATH(self):
        log_path = self.cfg.get('path', 'LOG_PATH')
        return log_path

    @property
    def REPORTS_PATH(self):
        reports_path = self.cfg.get('path', 'REPORTS_PATH')
        return reports_path

    @property
    def CASE_PATH(self):
        case_path = self.cfg.get('path', 'CASE_PATH')
        return case_path

    @property
    def LOG_LEVEL(self):
        log_level = int(self.cfg.get('log', 'LOG_LEVEL'))
        return log_level

    @property
    def SMTP_SERVER(self):
        smtp_server_value = self.cfg.get('email', 'smtp_server')
        return smtp_server_value

    @property
    def SMTP_SENDER(self):
        smtp_sender_value = self.cfg.get('email', 'smtp_sender')
        return smtp_sender_value

    @property
    def SMTP_PASSWORD(self):
        smtp_password_value = self.cfg.get('email', 'smtp_password')
        return smtp_password_value

    @property
    def SMTP_RECEIVER(self):
        smtp_receiver_value = self.cfg.get('email', 'smtp_receiver')
        return smtp_receiver_value

    @property
    def SMTP_CC(self):
        smtp_cc_value = self.cfg.get('email', 'smtp_cc')
        return smtp_cc_value

    @property
    def SMTP_SUBJECT(self):
        smtp_subject = self.cfg.get('email', 'smtp_subject')
        return smtp_subject


local_config = LocalConfigUtils()

if __name__ == '__main__':
    cfg = LocalConfigUtils()
    print(cfg.SMTP_SERVER)
    print(cfg.SMTP_SENDER)
    print(cfg.SMTP_PASSWORD)
    print(cfg.SMTP_RECEIVER)
    print(cfg.SMTP_CC)
    print(cfg.SMTP_SUBJECT)

