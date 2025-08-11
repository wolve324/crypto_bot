

import sys
from api_client import client
from logger_config import get_logger

logger = get_logger(__name__)

def place_oco_order(symbol, side, qty, take_profit_price, stop_price, stop_limit_price):
    try:
        logger.info({
            "action": "oco_order",
            "symbol": symbol,
            "side": side,
            "qty": qty,
            "take_profit_price": take_profit_price,
            "stop_price": stop_price,
            "stop_limit_price": stop_limit_price
        })

        # Place take profit limit order
        take_profit_order = client.futures_create_order(
            symbol=symbol,
            side=side.upper(),
            type="LIMIT",
            quantity=qty,
            price=str(take_profit_price),
            timeInForce="GTC"
        )
        logger.info({"action": "oco_take_profit_order", "response": take_profit_order})

        # Place stop loss stop-limit order
        stop_loss_order = client.futures_create_order(
            symbol=symbol,
            side=side.upper(),
            type="STOP",
            quantity=qty,
            price=str(stop_limit_price),
            stopPrice=str(stop_price),
            timeInForce="GTC"
        )
        logger.info({"action": "oco_stop_loss_order", "response": stop_loss_order})

        print("Take Profit Order:", take_profit_order)
        print("Stop Loss Order:", stop_loss_order)

    except Exception as e:
        logger.exception("OCO order failed")
        print(f"Error placing OCO order: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 7:
        print("Usage: python src/oco.py SYMBOL BUY/SELL QTY TAKE_PROFIT_PRICE STOP_PRICE STOP_LIMIT_PRICE")
        sys.exit(1)

    symbol = sys.argv[1]
    side = sys.argv[2]
    qty = float(sys.argv[3])
    take_profit_price = float(sys.argv[4])
    stop_price = float(sys.argv[5])
    stop_limit_price = float(sys.argv[6])

    place_oco_order(symbol, side, qty, take_profit_price, stop_price, stop_limit_price)
