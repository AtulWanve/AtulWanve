# Binance Futures Testnet Trading Bot

A simplified Python-based trading bot for Binance Futures (USDT-M) Testnet. This application supports placing Market and Limit orders via a Command Line Interface (CLI).

## Features
- **Market & Limit Orders**: Supports both BUY and SELL sides.
- **Structured Code**: Separated into client, order logic, validation, and CLI layers.
- **Robust Logging**: All API interactions and errors are logged to `logs/trading_bot.log`.
- **Input Validation**: Ensures all user inputs are valid before hitting the API.
- **Interactive Mode**: Bonus feature for a more user-friendly experience.

## Setup Instructions

### 1. Prerequisites
- Python 3.8+
- Binance Futures Testnet API Key and Secret.

### 2. Installation
Clone the repository and install dependencies:
```bash
pip install -r requirements.txt
```

### 3. Configuration
Create a `.env` file in the root directory and add your Binance Testnet credentials:
```env
BINANCE_API_KEY=your_api_key_here
BINANCE_API_SECRET=your_api_secret_here
```

## How to Run

### Using CLI Arguments
**Market Order:**
```bash
python cli.py order --symbol BTCUSDT --side BUY --type MARKET --quantity 0.001
```

**Limit Order:**
```bash
python cli.py order --symbol BTCUSDT --side SELL --type LIMIT --quantity 0.001 --price 60000
```

### Using Interactive Mode
```bash
python cli.py interactive
```

## Project Structure
```
trading_bot/
  bot/
    __init__.py
    client.py        # Binance client wrapper
    orders.py        # Order placement logic
    validators.py    # Input validation
    logging_config.py # Logging setup
  cli.py             # CLI entry point
  logs/              # Log files directory
  README.md
  requirements.txt
  .env               # Environment variables (ignored by git)
```

## Assumptions
- The bot is specifically designed for the Binance Futures USDT-M Testnet.
- Users have a valid testnet account with sufficient margin.
- The `python-binance` library is used for API interactions.
