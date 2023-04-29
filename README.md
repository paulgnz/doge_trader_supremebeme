# doge_trader_supremebeme
Buy and Sell DOGE on ProtonDEX / SuchDEX based on new twitter follower count.

I created a Python script that will BUY or SELL $DOGE using SuchDEX.com every time I gain or lose a follower on Twitter

Help test it out by following me! https://twitter.com/supremebeme

https://twitter.com/supremebeme/status/1652393427701727233

Call "python ./twitter_get_followers.py"

The script will check how many followers you have gained or lost since last check, then call the 'dex_buy_doge_limit.py' script with the arguments (order_side, amount)
