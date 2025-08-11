from api_client import client

def get_current_price(symbol):
    ticker = client.futures_symbol_ticker(symbol=symbol)
    print(f"Current price of {symbol}: {ticker['price']}")

if __name__ == "__main__":
    import sys
    if len(sys.argv) != 2:
        print("Usage: python src/get_price.py SYMBOL")
        sys.exit(1)
    get_current_price(sys.argv[1])
