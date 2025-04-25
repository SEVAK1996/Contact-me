from binance.client import Client

API_KEY = 'DitcXmd8eBFOm1zanlsxutLhZssDK2cuahtTLIQ54JJCIuKtboNEpk2yc9pS0gnu'
API_SECRET = 'oHb288vG1qr3PUsFQBFgE66QYCXqfiHcRygtSeW3iS08mFI4usdVoX1wv8U9bF5i'

client = Client(API_KEY, API_SECRET)

def place_order(symbol="BTCUSDT", side="BUY", quantity=0.001):
    try:
        order = client.create_test_order(
            symbol=symbol,
            side=side,
            type='MARKET',
            quantity=quantity
        )
        return "✅ Թեստ պատվերը հաջողությամբ ստեղծվեց"
    except Exception as e:
        return f"❌ Սխալ Binance-ում: {e}"