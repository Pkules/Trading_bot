import time
from bot.bot import TradingBot
from utils.notifications import send_discord_notification
from config.settings import API_KEY, API_SECRET

def main():
    try:
        # Initialize the trading bot
        bot = TradingBot(API_KEY, API_SECRET)
        
        # Start the main loop
        while True:
            try:
                # Get symbol pairs to trade
                symbol_pairs = bot.get_symbol_pairs()
                
                for symbol in symbol_pairs:
                    try:
                        buy_price, sell_price = bot.arbitrage_opportunity(symbol)
                        
                        if sell_price > buy_price:
                            bot.execute_arbitrage("Binance", "AnotherExchange", symbol, buy_price, sell_price)
                        
                        time.sleep(3)  # Sleep between checks to avoid rate limits
                    except Exception as e:
                        print(f"Exception in symbol loop: {e}")
                        time.sleep(3)  # Sleep in case of exception in symbol loop
            except Exception as e:
                print(f"Exception in main loop: {e}")
                time.sleep(3)  # Sleep in case of exception in main loop
    except KeyboardInterrupt:
        print("Bot stopped by user.")

if __name__ == "__main__":
    main()
