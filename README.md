# Binance Futures Order Bot

## Overview
This is a CLI-based trading bot for Binance USDT-M Futures.  
It supports multiple order types including Market, Limit, Stop-Limit, OCO, TWAP, and Grid orders.  
The bot validates user inputs, executes orders via Binance API, and logs all activities in a structured log file.

## Features
- Market Orders (Buy/Sell)
- Limit Orders (Buy/Sell at specified price)
- Stop-Limit Orders
- OCO Orders (One-Cancels-the-Other)
- TWAP Orders (Split large orders over time)
- Grid Orders (Automated buy/sell in a price range)
- Input validation for symbols, quantities, and prices
- Structured logging of all order actions and errors

## Setup Instructions

### Prerequisites
- Python 3.8 or higher
- `pip` package manager

### Installation
1. Clone the repo:
   ```bash
   git clone https://github.com/wolve324/crypto_bot.git
   cd crypto_bot
