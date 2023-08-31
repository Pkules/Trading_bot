# This code runs when the package is imported

# Import symbols from submodule files to make them available at the package level
from .order_book_analysis import analyze_order_book
from .notifications import send_discord_notification

# You can also provide a version variable or other package-level settings
__version__ = '1.0.0'
