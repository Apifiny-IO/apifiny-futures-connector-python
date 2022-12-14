# Apifiny Futures OPEN API Connector Python
[![GitHub issues](https://img.shields.io/github/issues/Apifiny-IO/apifiny-futures-connector-python)](https://github.com/Apifiny-IO/apifiny-futures-connector-python/issues)
[![GitHub forks](https://img.shields.io/github/forks/Apifiny-IO/apifiny-futures-connector-python)](https://github.com/Apifiny-IO/apifiny-futures-connector-python/network)
[![GitHub stars](https://img.shields.io/github/stars/Apifiny-IO/apifiny-futures-connector-python)](https://github.com/Apifiny-IO/apifiny-futures-connector-python/stargazers)
[![GitHub license](https://img.shields.io/github/license/Apifiny-IO/apifiny-futures-connector-python)](https://github.com/Apifiny-IO/apifiny-futures-connector-python/blob/main/LICENSE)
[![contributors](https://img.shields.io/github/contributors/Apifiny-IO/apifiny-futures-connector-python)](https://github.com/Apifiny-IO/apifiny-futures-connector-python/graphs/contributors)
[![PyPI](https://img.shields.io/pypi/v/apifiny-futures)](https://pypi.org/project/apifiny-futures/)
[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/apifiny-futures)](https://pypi.org/project/apifiny-futures/)
[![Downloads](https://pepy.tech/badge/apifiny-futures)](https://pepy.tech/project/apifiny-futures)

This is a library that works as a connector to [APIFINY FUTURES OPEN API](https://github.com/Apifiny-IO/apifiny-futures-connector-python)

- Supported APIs:
>- REST trading/market API
>- WebSocket market API


## OPEN API Documentation

[https://doc.apifiny.com/futures/#introduction](https://doc.apifiny.com/futures/#introduction)


## Install
```bash
pip3 install -U apifiny-futures
```

## RESTful APIs
**Usage examples:**

Get all supported exchanges
```python
from apifiny_futures.rest_api import API as Client

client = Client(venue="BINANCE")
print(client.list_venue())
```
Get Market Data
```python
from apifiny_futures.rest_market import MarketData as Client

client = Client()
# Get BINANCE orderbook of BTCUSDT
print(client.get_order_book("BINANCE", "BTCUSDT"))
```
Create Order
```python
from apifiny_futures.rest_api import API as Client

# If you get the error:"Timestamp for this request is outside of the recvWindow", 
# you can calibrate local time or set recv_window
# api key/secret are required for trade endpoints
client = Client(venue="BINANCE", key='<api_key>', secret='<api_secret>', recv_window=10000)

# Post a new order
params = {
    "accountId": '<account_id>',
    "venue": '<venue>',
    "orderInfo":{
        "symbol":"BTCUSDT",
        "orderType":"TRAILING",
        "timeInForce":"GTC",
        "orderSide":"SELL",
        "price":"100",
        "qty":"0.1",
        "stopPrice":"0",
        "workingType":"CONTRACT_PRICE",
        "positionSide":"BOTH",
        "reduceOnly":"false",
        "closePosition":"false",
        "activationPrice":"9020",
        "callbackRate":"0.1",
        "priceProtect":"false"
    }
}

resp = client.new_order(**params)
print(resp)
```

## WebSocket APIs

**Usage examples:**

Subscribe Market Data
```python
from apifiny_futures.fut_websocket import FutApi as Client

# Get BINANCE orderbook of BTCUSDT
msg = {"channel": "orderbook", "symbol": 'BTCUSDT', "venues": ["BINANCE"], "action": "sub"}
# Get BINANCE klines of BTCUSDT at 1m interval
# msg = {"channel": "kline_1m", "symbol": "BTCUSDT", "venues": ["BINANCE"], "action": "sub"}
client = Client()
client.connect(md=True)
client.send_msg(msg)
```
pushing data
```python
from apifiny_futures.fut_websocket import FutApi as Client

# api key/secret are required for subscribe order and asset update
client = Client(venue="BINANCE")
client.connect()
client.login('<api_key_id>', '<secret_key>')
```

Please find `examples` folder to check for more endpoints.


## Contributing

Contributions are welcome.<br/>
If you've found a bug within this project, please open an issue to discuss what you would like to change.<br/>
If it's an issue with the API, please report any new issues at [apifiny-futures-connector-python issues](https://github.com/Apifiny-IO/apifiny-futures-connector-python/issues)