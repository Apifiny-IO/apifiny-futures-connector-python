#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
====================================
@File    :  base_info.py
@Time    :  2022/07/12 15:40:29
@Author  :  LiuKeCode@hotmail.com
@Desc    :  None
====================================
"""
# here put the import lib

import logging
from apifiny_futures.rest_api import API as Client
from apifiny_futures.lib.utils import config_logging

config_logging(logging, logging.INFO)

venue = "BINANCE"

client = Client(venue)

logging.info(client.list_venue())
logging.info(client.list_symbol(venue))
logging.info(client.list_currency(venue))
