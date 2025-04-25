import requests
import os
from binance.client import Client

def check_and_trade():
    print("▶️ Running Scanner...")

    # CoinGecko BTC գին
    url = "https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=usd"
    r = requests.get(url)
    price = r.json()["bitcoin"]["usd"]

    print(f"BTC Price: ${price}")

    # Binance Auth
    api_key = os.getenv("BINANCE_API_KEY")
    api_secret = os.getenv("BINANCE_SECRET_KEY")
    client = Client(api_key, api_secret)

    # Պայմաններ
    symbol = "BTCUSDT"
    qty = 0.001  # փոխի ըստ քո գումարի

    if price > 70000:
        client.futures_create_order(symbol=symbol, side="BUY", type="MARKET", quantity=qty)
        print("Opened LONG BTC")
    elif price < 60000:
        client.futures_create_order(symbol=symbol, side="SELL", type="MARKET", quantity=qty)
        print("Opened SHORT BTC")
    else:
        print("No trade signal")
