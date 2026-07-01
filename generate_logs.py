import unittest
from unittest.mock import MagicMock, patch
from bot.orders import OrderManager
import os

def generate_sample_logs():
    print("Generating sample logs via mocked API calls...")
    
    # Mock responses
    market_response = {
        'orderId': 12345678,
        'symbol': 'BTCUSDT',
        'status': 'FILLED',
        'executedQty': '0.001',
        'avgPrice': '65000.00',
        'side': 'BUY',
        'type': 'MARKET'
    }
    
    limit_response = {
        'orderId': 87654321,
        'symbol': 'BTCUSDT',
        'status': 'NEW',
        'executedQty': '0.000',
        'avgPrice': '0.00',
        'price': '60000.00',
        'side': 'SELL',
        'type': 'LIMIT'
    }

    with patch('binance.client.Client.futures_create_order') as mock_order:
        # Setup manager
        manager = OrderManager(api_key="mock_key", api_secret="mock_secret")
        
        # 1. Generate MARKET order log
        print("\n--- Simulating MARKET Order ---")
        mock_order.return_value = market_response
        manager.execute_order("BTCUSDT", "BUY", "MARKET", 0.001)
        
        # 2. Generate LIMIT order log
        print("\n--- Simulating LIMIT Order ---")
        mock_order.return_value = limit_response
        manager.execute_order("BTCUSDT", "SELL", "LIMIT", 0.001, 60000)

if __name__ == "__main__":
    generate_sample_logs()
