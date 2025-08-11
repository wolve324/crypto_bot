import logging
from api_client import client
from logger_config import get_logger

logger = get_logger(__name__)

def place_limit_order(symbol, side, qty, price):
    try:
        logger.info({'action': 'limit_order', 'symbol': symbol, 'side': side, 'qty': qty, 'price': price})
        order = client.futures_create_order(
            symbol=symbol,
            side=side.upper(),
            type='LIMIT',
            timeInForce='GTC',
            quantity=qty,
            price=str(price)
        )
        logger.info({'action': 'limit_order_result', 'response': order})
        print(f"Placed limit {side} order: {qty} {symbol} @ {price}")
    except Exception as e:
        logger.exception("Limit order failed")
        print(f"Error placing limit order: {e}")

def create_grid_orders(symbol, total_qty, lower_price, upper_price, grid_levels):
    price_step = (upper_price - lower_price) / grid_levels
    qty_per_order = total_qty / grid_levels

    # Place buy orders from lower_price upwards
    for i in range(grid_levels):
        price = lower_price + i * price_step
        place_limit_order(symbol, 'BUY', qty_per_order, price)

    # Place sell orders from upper_price downwards
    for i in range(grid_levels):
        price = upper_price - i * price_step
        place_limit_order(symbol, 'SELL', qty_per_order, price)

if __name__ == "__main__":
    import sys
    if len(sys.argv) != 6:
        print("Usage: python src/grid_orders.py SYMBOL TOTAL_QTY LOWER_PRICE UPPER_PRICE GRID_LEVELS")
        sys.exit(1)

    symbol = sys.argv[1]
    total_qty = float(sys.argv[2])
    lower_price = float(sys.argv[3])
    upper_price = float(sys.argv[4])
    grid_levels = int(sys.argv[5])

    create_grid_orders(symbol, total_qty, lower_price, upper_price, grid_levels)
