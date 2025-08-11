import logging
import re

# Logger setup
logger = logging.getLogger("binance_bot")
logger.setLevel(logging.DEBUG)

# Create file handler which logs messages
file_handler = logging.FileHandler("bot.log")
file_handler.setLevel(logging.DEBUG)

# Create console handler for output to console
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.INFO)

# Formatter for logs
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')

file_handler.setFormatter(formatter)
console_handler.setFormatter(formatter)

# Add handlers to logger
logger.addHandler(file_handler)
logger.addHandler(console_handler)


# Validation functions

def validate_symbol(symbol: str) -> bool:
    """Validate symbol format, e.g., BTCUSDT, ETHUSDT."""
    # Basic pattern: 6-12 uppercase letters, usually ends with USDT or similar
    pattern = r'^[A-Z]{6,12}$'
    if re.match(pattern, symbol):
        return True
    logger.error(f"Invalid symbol format: {symbol}")
    return False


def validate_quantity(qty: float) -> bool:
    """Validate quantity is positive and reasonable."""
    if qty > 0:
        return True
    logger.error(f"Invalid quantity: {qty}. Must be positive.")
    return False


def validate_price(price: float) -> bool:
    """Validate price is positive."""
    if price > 0:
        return True
    logger.error(f"Invalid price: {price}. Must be positive.")
    return False
