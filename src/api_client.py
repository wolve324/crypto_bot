import os
from dotenv import load_dotenv
from binance.client import Client

# Explicitly load .env from project root
env_path = os.path.join(os.path.dirname(__file__), '..', '.env')
load_dotenv(dotenv_path=env_path)

API_KEY = os.getenv("BINANCE_API_KEY")
API_SECRET = os.getenv("BINANCE_API_SECRET")
USE_TESTNET = os.getenv("USE_TESTNET", "True").lower() == "true"
print(f"API Key: '{API_KEY}'")
print(f"API Secret: '{API_SECRET}'")

if not API_KEY or not API_SECRET:
    raise ValueError("❌ Missing Binance API credentials in .env file!")

client = Client(API_KEY, API_SECRET, testnet=USE_TESTNET)

if USE_TESTNET:
    # Set testnet futures URL explicitly for python-binance
    client.FUTURES_URL = "https://testnet.binancefuture.com/fapi"
