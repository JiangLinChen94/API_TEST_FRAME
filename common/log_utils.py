#!/usr/bin/env python
# encoding: utf-8
# @author: Alin
# @file: .py
# @time: 2020/7/11 11:40

import os
import logging
import time
from common.local_config_utils import local_config

current_path = os.path.dirname(__file__)
log_out_path = os.path.join(current_path, '..', local_config.LOG_PATH)


class LogUtils():
    def __init__(self, log_path=log_out_path):
        self.log_name = os.path.join(log_out_path, 'APITest_%s.log' % time.strftime("%Y_%m_%d"))
        self.logger = logging.getLogger("APITest")
        self.logger.setLevel(local_config.LOG_LEVEL)

        console_handler = logging.StreamHandler()
        file_handler = logging.FileHandler(self.log_name, 'a', encoding='utf-8')
        formatter = logging.Formatter(
            '[%(asctime)s] %(filename)s->%(funcName)s line:%(lineno)d [%(levelname)s] : %(message)s'
            )
        console_handler.setFormatter(formatter)
        file_handler.setFormatter(formatter)

        self.logger.addHandler(console_handler)
        self.logger.addHandler(file_handler)

        console_handler.close()
        file_handler.close()

    def get_logger(self):
        return self.logger


logger = LogUtils().get_logger()

if __name__ == '__main__':
    logger.info('hello')
