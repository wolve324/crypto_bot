import sys
from api_client import client
from validators import validate_symbol, validate_side, validate_qty, validate_price
from logger_config import get_logger

logger = get_logger(__name__)

def place_stop_limit_order(symbol, side, qty, stop_price, limit_price):
    if not validate_symbol(symbol):
        raise ValueError("Invalid symbol format")
    if not validate_side(side):
        raise ValueError("Side must be BUY or SELL")
    if not validate_qty(qty):
        raise ValueError("Quantity must be a positive number")
    if not validate_price(stop_price):
        raise ValueError("Stop price must be positive")
    if not validate_price(limit_price):
        raise ValueError("Limit price must be positive")

    logger.info({
        "action": "stop_limit_order",
        "symbol": symbol,
        "side": side,
        "qty": qty,
        "stop_price": stop_price,
        "limit_price": limit_price
    })

    try:
        order = client.futures_create_order(
            symbol=symbol,
            side=side.upper(),
            type="STOP",
            quantity=qty,
            price=str(limit_price),
            stopPrice=str(stop_price),
            timeInForce="GTC"
        )
        logger.info({"action": "stop_limit_order_result", "response": order})
        print(order)
    except Exception as e:
        logger.exception("Stop-Limit order failed")
        print(f"Error placing stop-limit order: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 6:
        print("Usage: python src/stop_limit_orders.py SYMBOL BUY/SELL QTY STOP_PRICE LIMIT_PRICE")
        sys.exit(1)

    symbol = sys.argv[1]
    side = sys.argv[2]
    qty = float(sys.argv[3])
    stop_price = float(sys.argv[4])
    limit_price = float(sys.argv[5])

    place_stop_limit_order(symbol, side, qty, stop_price, limit_price)
