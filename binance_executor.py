from binance.client import Client
import os

# Բանալի տվյալները
API_KEY = os.getenv("BINANCE_API_KEY")
API_SECRET = os.getenv("BINANCE_SECRET")

client = Client(API_KEY, API_SECRET)

def place_order(symbol, side="BUY", quantity=0.01, leverage=3):
    try:
        # Սահմանում ենք լիվերիջ
        client.futures_change_leverage(symbol=symbol, leverage=leverage)

        # Վարկանշային գործարք
        order = client.futures_create_order(
            symbol=symbol,
            side=side,
            type='MARKET',
            quantity=quantity
        )
        print(f"{side} order placed: {order}")
        return order

    except Exception as e:
        print(f"Error placing order: {e}")
        return None

# Օրինակ օգտագործում
if __name__ == "__main__":
    # BTCUSDT LONG
    place_order("BTCUSDT", side="BUY", quantity=0.01, leverage=5)

    # ETHUSDT SHORT
    # place_order("ETHUSDT", side="SELL", quantity=0.05, leverage=3)
