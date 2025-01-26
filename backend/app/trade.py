portfolio = {
    'cash': 10000,  # Initial cash balance
    'stocks': {},  # Stock holdings
    'trade_history': []  # Log of trades
}

def portfolio_reset():
    portfolio['cash'] = 10000
    portfolio['stocks'] = {}
    portfolio['trade_history'] = []


def execute_trade(portfolio, symbol, action, quantity, price):
    if action == 'BUY':
        total_cost = quantity * price
        if portfolio['cash'] >= total_cost:
            portfolio['cash'] -= total_cost
            portfolio['stocks'][symbol] = portfolio['stocks'].get(symbol, 0) + quantity
            portfolio['trade_history'].append((symbol, action, quantity, price))
            return {'status': 'success', 'message': 'Trade executed'}
        else:
            return {'status': 'failure', 'message': 'Insufficient funds'}
    elif action == 'SELL':
        if portfolio['stocks'].get(symbol, 0) >= quantity:
            portfolio['stocks'][symbol] -= quantity
            portfolio['cash'] += quantity * price
            portfolio['trade_history'].append((symbol, action, quantity, price))
            return {'status': 'success', 'message': 'Trade executed'}
        else:
            return {'status': 'failure', 'message': 'Not enough shares'}

def calculate_portfolio_value(portfolio, live_prices, day):
    total_value = portfolio['cash']
    for symbol, quantity in portfolio['stocks'].items():
        total_value += quantity * live_prices[symbol][day]
    return total_value