from binance.client import Client
from config.settings import API_KEY, API_SECRET
from risk_management import RiskManager
from trading_strategy import TradingStrategy

def main():
    client = Client(API_KEY, API_SECRET)
    
    # Create a RiskManager instance with your risk management parameters
    risk_manager = RiskManager(
        max_position_percentage=0.01,
        target_profit_percentage=0.5,
        trading_fee_percentage=0.1,
        min_order_quantity=0.001,  # Adjust as needed
        slippage_percentage=0.005   # Adjust as needed
    )
    
    # Create a TradingStrategy instance with the RiskManager and Binance client
    trading_strategy = TradingStrategy(risk_manager, client, price_threshold_percentage=0.002)
    
    # Define the symbol pairs you want to trade
    symbol_pairs = ['XRPBTC', 'TRXBTC']
    
    # Start the main trading loop
    while True:
        try:
            for symbol in symbol_pairs:
                trading_strategy.execute_strategy(symbol)
            
            # Sleep between checks to avoid rate limits
            time.sleep(3)
            
        except Exception as e:
            print(f"Exception: {e}")
            time.sleep(3)

if __name__ == "__main__":
    main()
