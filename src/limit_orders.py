import sys
from api_client import client
from validators import validate_symbol, validate_side, validate_qty, validate_price
from logger_config import get_logger

logger = get_logger(__name__)

def place_limit_order(symbol, side, qty, price):
    if not validate_symbol(symbol):
        raise ValueError("Invalid symbol format")
    if not validate_side(side):
        raise ValueError("Side must be BUY or SELL")
    if not validate_qty(qty):
        raise ValueError("Quantity must be a positive number")
    if not validate_price(price):
        raise ValueError("Price must be a positive number")

    logger.info({"action": "limit_order", "symbol": symbol, "side": side, "qty": qty, "price": price})
    try:
        order = client.futures_create_order(
            symbol=symbol,
            side=side.upper(),
            type="LIMIT",
            quantity=qty,
            price=str(price),  # price must be string for Binance API
            timeInForce="GTC"  # Good Till Cancelled
        )
        logger.info({"action": "limit_order_result", "response": order})
        print(order)
    except Exception as e:
        logger.exception("Limit order failed")
        print(f"Error placing limit order: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 5:
        print("Usage: python src/limit_orders.py SYMBOL BUY/SELL QTY PRICE")
        sys.exit(1)

    symbol = sys.argv[1]
    side = sys.argv[2]
    qty = float(sys.argv[3])
    price = float(sys.argv[4])

    place_limit_order(symbol, side, qty, price)
