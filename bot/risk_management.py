class RiskManager:
    def __init__(self, max_position_percentage, target_profit_percentage, trading_fee_percentage, min_order_quantity, slippage_percentage):
        self.max_position_percentage = max_position_percentage
        self.target_profit_percentage = target_profit_percentage
        self.trading_fee_percentage = trading_fee_percentage
        self.min_order_quantity = min_order_quantity
        self.slippage_percentage = slippage_percentage

    def calculate_order_quantity(self, balance, buy_price, sell_price, symbol_step_size):
        # Apply slippage to buy price and sell price
        adjusted_buy_price = buy_price * (1 + self.slippage_percentage)
        adjusted_sell_price = sell_price * (1 - self.slippage_percentage)
        
        max_order_quantity = (balance * self.max_position_percentage) / adjusted_buy_price
        
        order_quantity = (max_order_quantity * self.target_profit_percentage) / adjusted_sell_price
        
        trading_fee = (order_quantity * adjusted_sell_price) * self.trading_fee_percentage
        order_quantity -= trading_fee
        
        min_order_quantity = self.min_order_quantity / adjusted_sell_price
        order_quantity = max(order_quantity, min_order_quantity)
        
        rounded_order_quantity = self.round_quantity(order_quantity, symbol_step_size)
        
        if rounded_order_quantity < symbol_step_size:
            return None
        return rounded_order_quantity

    def round_quantity(self, quantity, step_size):
        return round(quantity / step_size) * step_size
