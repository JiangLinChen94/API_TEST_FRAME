#!/usr/bin/env python
# encoding: utf-8
# @author: Alin
# @file: .py
# @time: 2020/7/5 11:53

import os
from common.config_utils import ConfigUtils

config_path = os.path.join(os.path.dirname(__file__), '..', 'conf/config.ini')

configUtils = ConfigUtils(config_path)

URL = configUtils.read_value('default', 'URL')
CASE_DATA_PATH = configUtils.read_value('path', 'CASE_DATA_PATH')
