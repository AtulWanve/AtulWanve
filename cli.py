import argparse
import sys
from bot.orders import OrderManager
from dotenv import load_dotenv

def main():
    load_dotenv()
    
    parser = argparse.ArgumentParser(description="Binance Futures Testnet Trading Bot CLI")
    
    # Subcommands
    subparsers = parser.add_subparsers(dest="command", help="Available commands")
    
    # Order command
    order_parser = subparsers.add_parser("order", help="Place a new order")
    order_parser.add_argument("--symbol", required=True, help="Trading symbol (e.g., BTCUSDT)")
    order_parser.add_argument("--side", required=True, choices=["BUY", "SELL"], help="Order side")
    order_parser.add_argument("--type", required=True, choices=["MARKET", "LIMIT"], help="Order type")
    order_parser.add_argument("--quantity", required=True, type=float, help="Order quantity")
    order_parser.add_argument("--price", type=float, help="Price (required for LIMIT orders)")
    
    # Interactive command (Bonus)
    subparsers.add_parser("interactive", help="Start interactive menu")
    
    args = parser.parse_args()
    
    if args.command == "order":
        manager = OrderManager()
        manager.execute_order(
            symbol=args.symbol,
            side=args.side,
            order_type=args.type,
            quantity=args.quantity,
            price=args.price
        )
    elif args.command == "interactive":
        start_interactive_menu()
    else:
        parser.print_help()

def start_interactive_menu():
    print("\n--- Binance Futures Bot Interactive Menu ---")
    try:
        symbol = input("Enter Symbol (e.g. BTCUSDT): ").strip().upper()
        side = input("Enter Side (BUY/SELL): ").strip().upper()
        order_type = input("Enter Type (MARKET/LIMIT): ").strip().upper()
        quantity = input("Enter Quantity: ").strip()
        price = None
        if order_type == "LIMIT":
            price = input("Enter Price: ").strip()
        
        manager = OrderManager()
        manager.execute_order(
            symbol=symbol,
            side=side,
            order_type=order_type,
            quantity=quantity,
            price=price
        )
    except KeyboardInterrupt:
        print("\nExiting...")
        sys.exit(0)
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
