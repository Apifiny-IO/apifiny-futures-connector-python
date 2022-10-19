#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
====================================
@File    :  market_data.py
@Time    :  2022/07/12 15:39:49
@Author  :  LiuKeCode@hotmail.com
@Desc    :  None
====================================
"""
# here put the import lib

import logging
from apifiny_futures.rest_market import MarketData as Client
from apifiny_futures.lib.utils import config_logging

config_logging(logging, logging.INFO)

venue = "BINANCE"
symbol = "BTCUSDT"

client = Client()

logging.info(client.get_mark(venue, symbol))
# logging.info(client.get_order_book(venue, symbol))
# logging.info(client.get_ticker(venue, symbol))
# logging.info(client.get_trade(venue, symbol))
# logging.info(client.get_kline(venue, "BTC", "USDT", "1m"))
