import time
from api_client import client
from logger_config import get_logger

logger = get_logger(__name__)

def place_market_order(symbol, side, qty):
    try:
        logger.info({'action': 'market_order', 'symbol': symbol, 'side': side, 'qty': qty})
        order = client.futures_create_order(
            symbol=symbol,
            side=side.upper(),
            type='MARKET',
            quantity=qty
        )
        logger.info({'action': 'market_order_result', 'response': order})
        print(f"Executed market order: {order}")
    except Exception as e:
        logger.exception("Market order failed")
        print(f"Error placing market order: {e}")

def twap_order(symbol, side, total_qty, duration_sec, intervals):
    qty_per_order = total_qty / intervals
    interval_delay = duration_sec / intervals

    logger.info({
        'action': 'twap_order_start',
        'symbol': symbol,
        'side': side,
        'total_qty': total_qty,
        'duration_sec': duration_sec,
        'intervals': intervals,
        'qty_per_order': qty_per_order,
        'interval_delay': interval_delay
    })

    for i in range(intervals):
        print(f"Placing order {i+1} of {intervals}, qty: {qty_per_order}")
        place_market_order(symbol, side, qty_per_order)
        if i < intervals - 1:
            time.sleep(interval_delay)

    logger.info({'action': 'twap_order_completed'})

if __name__ == "__main__":
    import sys
    if len(sys.argv) != 6:
        print("Usage: python src/twap.py SYMBOL BUY/SELL TOTAL_QTY DURATION_SECONDS INTERVALS")
        sys.exit(1)

    symbol = sys.argv[1]
    side = sys.argv[2]
    total_qty = float(sys.argv[3])
    duration_sec = int(sys.argv[4])
    intervals = int(sys.argv[5])

    twap_order(symbol, side, total_qty, duration_sec, intervals)
