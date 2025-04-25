import requests
import time

def get_btc_eth_price_changes():
    url = "https://api.coingecko.com/api/v3/simple/price"
    params = {
        "ids": "bitcoin,ethereum",
        "vs_currencies": "usd",
        "include_24hr_change": "true"
    }

    try:
        response = requests.get(url, params=params)
        data = response.json()

        btc_change = data["bitcoin"]["usd_24h_change"]
        eth_change = data["ethereum"]["usd_24h_change"]

        return btc_change, eth_change

    except Exception as e:
        print(f"Error fetching CoinGecko data: {e}")
        return None, None

# Օրինակ օգտագործում
if __name__ == "__main__":
    while True:
        def check_and_trade():
    print("▶️ CoinGecko Scanner launched")
    # այստեղ մնացած կոդը...
        btc, eth = get_btc_eth_price_changes()
        if btc is not None:
            print(f"BTC 24h change: {btc:.2f}%")
            print(f"ETH 24h change: {eth:.2f}%")

            if abs(btc) > 5:
                print("Smart Signal: BTC spike detected!")

            if abs(eth) > 5:
                print("Smart Signal: ETH spike detected!")
        
        time.sleep(60)
