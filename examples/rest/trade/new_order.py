#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
====================================
@File    :  new_order.py
@Time    :  2022/07/18 14:42:27
@Author  :  LiuKeCode@hotmail.com
@Desc    :  None
====================================
"""
# here put the import lib

import logging
from apifiny_futures.rest_api import API as Client
from apifiny_futures.lib.utils import config_logging
from apifiny_futures.lib.utils import generate_orderid

config_logging(logging, logging.INFO)

account_id = ""
api_key_id = ""
secret_key = ""

unified_url = False
venue = "BINANCE"

# LIMIT
params = {
    "accountId": account_id,
    "venue": venue,
    "clientOrderId": generate_orderid(account_id),
    "orderInfo": {
        "symbol": "BTCUSDT",
        "orderType": "TRAILING",
        "timeInForce": "GTC",
        "orderSide": "SELL",
        "price": "100",
        "qty": "0.1",
        "stopPrice": "0",
        "workingType": "CONTRACT_PRICE",
        "positionSide": "BOTH",
        "reduceOnly": "false",
        "closePosition": "false",
        "activationPrice": "9020",
        "callbackRate": "0.1",
        "priceProtect": "false"
    }
}
# MARKET BUY
# "orderInfo": {"orderSide": "BUY", "orderType": "MARKET", "symbol": "BTCUSDT", "total": "xx"}
# MARKET SELL
# "orderInfo": {"orderSide": "SELL", "orderType": "MARKET", "symbol": "BTCUSDT", "quantity": "xx"}
# STOP stopType = LOSS or ENTRY
# "orderInfo": {"limitPrice": "xx", "orderSide": "BUY", "orderType": "STOP",  "quantity": "xx",
#               "symbol": "BTCUSDT", "timeInForce": 1, "stopType": "LOSS", "triggerPrice": "xx"}
# SOR: unified_url = True
# "orderInfo": {"limitPrice": "xx", "orderSide": "BUY", "orderType": "SOR",  "quantity": "xx",
#               "symbol": "BTCUSDT", "timeInForce": 1}

client = Client(venue, api_key_id, secret_key)

try:
    response = client.new_order(**params)
    logging.info(response)
except Exception as e:
    logging.error(e)
    raise
