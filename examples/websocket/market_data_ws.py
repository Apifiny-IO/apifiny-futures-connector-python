#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
====================================
@File    :  market_data_ws.py
@Time    :  2022/07/18 14:48:46
@Author  :  LiuKeCode@hotmail.com
@Contact :  email
@Desc    :  None
====================================
"""
# here put the import lib

from apifiny_futures.fut_websocket import FutApi as Client

msg = {"channel": "orderbook", "symbol": 'BTCUSDT', "venues": ["BINANCE"], "action": "sub"}

"""
# mark
{"channel": "mark", "symbol": "BTCUSDT", "venues": ["BINANCE"], "action": "sub"}
# Ticker Channel
{"channel": "ticker", "symbol": "BTCUSDT", "venues": ["BINANCE"], "action": "sub"}
# Trades Channel
{"channel": "trade", "symbol": "BTCUSDT", "venues": ["BINANCE"], "action": "sub"}
# OHLCV Channel
{"channel": "kline_1m", "symbol": "BTCUSDT", "venues": ["BINANCE"], "action": "sub"}
"""

client = Client()
client.connect(md=True)
client.send_msg(msg)
