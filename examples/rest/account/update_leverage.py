#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
====================================
@File    :  update_leverage.py
@Time    :  2022/07/18 15:26:39
@Author  :  LiukeCode@hotmail.com
@Desc    :  None
====================================
"""
# here put the import lib

import logging
from apifiny_futures.rest_api import API as Client
from apifiny_futures.lib.utils import config_logging

config_logging(logging, logging.INFO)

account_id = ""
api_key_id = ""
secret_key = ""

venue = ""

params = {
    "accountId": account_id,
    "venue": venue,
    "symbol": "BTCUSDT",
    "leverage": 2,
}

client = Client(venue, api_key_id, secret_key)

try:
    response = client.update_leverage(**params)
    logging.info(response)
except Exception as e:
    logging.error(e)
    raise
