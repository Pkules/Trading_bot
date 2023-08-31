# This code runs when the package is imported

# Import symbols from submodule files to make them available at the package level
from .bot import TradingBot
from .trading_strategy import implement_trading_strategy
from .risk_management import calculate_order_quantity