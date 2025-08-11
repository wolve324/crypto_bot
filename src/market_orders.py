import sys
from api_client import client
from validators import validate_symbol, validate_side, validate_qty
from logger_config import get_logger

logger = get_logger(__name__)

def place_market_order(symbol, side, qty):
    if not validate_symbol(symbol): raise ValueError("Invalid symbol")
    if not validate_side(side): raise ValueError("Invalid side")
    if not validate_qty(qty): raise ValueError("Invalid quantity")

    logger.info({"action": "market_order", "symbol": symbol, "side": side, "qty": qty})
    try:
        order = client.futures_create_order(
            symbol=symbol,
            side=side.upper(),
            type="MARKET",
            quantity=qty
        )
        logger.info({"action": "market_order_result", "response": order})
        print(order)
    except Exception as e:
        logger.exception("Market order failed")
        raise

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python src/market_orders.py SYMBOL BUY/SELL QTY")
        sys.exit(1)
    place_market_order(sys.argv[1], sys.argv[2], float(sys.argv[3]))
