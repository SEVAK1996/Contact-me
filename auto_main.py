import time
from coingecko_scanner import check_and_trade
from binance_executor import place_order

# Մետաղադրամ ընտրություն՝ կարող ես ավելացնել քոները
ASSETS = ["BTCUSDT"]
INTERVAL = 60 * 20  # Ստուգել ամեն 20 րոպեն մեկ

def auto_loop():
    print("🤖 Սկսում ենք ավտոտրեյդը... (Ctrl+C դադարեցնելու համար)")
    while True:
        print("🔍 Ստուգում ենք շուկան...")
        result = check_and_trade()
        print("📊 Վերլուծություն:", result)

        if "📉 BTC գինը ցածր է" in result:
            print("🚀 Բացում ենք LONG (թեստային)...")
            response = place_order(symbol="BTCUSDT", side="BUY", quantity=0.001)
            print("🟢 Binance պատասխանը:", response)

        elif "📈 BTC-ն բարձր է" in result:
            print("🔻 Բացում ենք SHORT (թեստային)...")
            response = place_order(symbol="BTCUSDT", side="SELL", quantity=0.001)
            print("🔴 Binance պատասխանը:", response)

        print("⏱ Հաջորդ ստուգումը կլինի 20 րոպե հետո...")
        time.sleep(INTERVAL)

if __name__ == "__main__":
    auto_loop()