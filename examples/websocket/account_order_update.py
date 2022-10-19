#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
====================================
@File    :  account_order_update.py
@Time    :  2022/07/12 15:42:10
@Author  :  LiuKeCode@hotmail.com
@Desc    :  None
====================================
"""
# here put the import lib

from apifiny_futures.fut_websocket import FutApi as Client

account_id = ""
api_key_id = ""
secret_key = ""

venue = "BINANCE"

client = Client(venue=venue)
# order and asset stream
client.connect()
client.login(api_key_id, secret_key)
