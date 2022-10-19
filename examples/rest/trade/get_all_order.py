#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
====================================
@File    :  get_all_orders.py
@Time    :  2022/07/18 14:41:28
@Author  :  LiuKeCode@hotmail.com
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

venue = "BINANCE"

params = {
    "accountId": account_id,
    "venue": venue
}

client = Client(venue, api_key_id, secret_key)

try:
    response = client.get_all_orders(**params)
    logging.info(response)
except Exception as e:
    logging.error(e)
    raise
