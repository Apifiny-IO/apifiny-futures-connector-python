#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
====================================
@File    :  query_fund_list.py
@Time    :  2022/07/18 15:43:32
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

venue = "BINANCE"

params = {
    "accountId": account_id,
    "venue": venue,
    "symbol": "BTCUSDT",
    "type": "REALIZED_PNL",
    "startTime": 1658073600,
    "endTime": 1658160000,
    "limit": 100,
}

client = Client(venue, api_key_id, secret_key)

try:
    response = client.get_fund_list(**params)
    logging.info(response)
except Exception as e:
    logging.error(e)
    raise
