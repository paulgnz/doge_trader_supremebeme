# doge_trader_supremebeme
Buy and Sell DOGE on ProtonDEX / SuchDEX based on new twitter follower count.

I created a Python script that will BUY or SELL $DOGE using [SuchDEX.com](https://SuchDEX.com) every time I gain or lose a follower on Twitter

It uses [Proton DEX](https://protondex.com/dex?referrer=paul) order books and API, you need a [WebAuth](https://WebAuth.com) wallet to start.

Deposit stablecoin to WebAuth wallet and Mint XMD [here](https://metaldollar.com).

Help test it out by following me! https://twitter.com/supremebeme

https://twitter.com/supremebeme/status/1652393427701727233

If you want to run this script yourself, make sure you have access to [twitter api](https://developer.twitter.com/)

Replace the following values in `twitter_get_followers.py` with your own API keys and access tokens
```
    consumer_key = 'api key'
    consumer_secret = 'api secret'
    access_token = 'access token'
    access_token_secret = 'access secret'
```
Insert your private key on line 29 of `dex_buy_doge_limit.py`
```
    wallet.import_key('mywallet', 'INSERT YOUR PVT KEY HERE')
```

Add your Proton username on line 37 of `dex_buy_doge_limit.py`
```
    USERNAME = 'trading.paul'
```

Then Call 
```
python ./twitter_get_followers.py
```

The script will check how many followers you have gained or lost since last check, then call the `dex_buy_doge_limit.py` script with the arguments `(order_side, amount)`

You can buy or sell XDOGE manually using the dex_buy_doge_limit script manually...

This will buy 1 XMD worth of DOGE

```
python ./dex_buy_doge_limit.py buy 1
```
and this will sell 1 XMD worth of DOGE

```
python ./dex_buy_doge_limit.py sell 1
```
