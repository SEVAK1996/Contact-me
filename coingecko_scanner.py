import requests

def check_and_trade():
    try:
        r = requests.get("https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=usd")
        data = r.json()
        price = data["bitcoin"]["usd"]
        if price < 30000:
            return f"📉 BTC գինը ցածր է 30K → ${price}"
        else:
            return f"📈 BTC-ն բարձր է 30K → ${price}"
    except Exception as e:
        return f"❌ Սխալ CoinGecko-ում: {e}"