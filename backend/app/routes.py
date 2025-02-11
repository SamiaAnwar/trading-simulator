from flask import Blueprint, request, jsonify
from app.backtesting import trades, portfolio_value, compare_predictions
app_routes = Blueprint('app_routes', __name__)

@app_routes.route('/live/scheduled_update', methods=['PUT'])
def scheduled_update():
    #TODO: Make a decision 
    #TODO: Update the databases 
    return 

@app_routes.route('/live/portfolio', methods=['GET', 'POST'])
def get_live_portfolio():
    #TODO: Fetch from portfolio table   
    return 

@app_routes.route('/live/value_history', methods=['GET', 'POST'])
def get_value_history():
    #TODO: Fetch from value history table  
    return 

@app_routes.route('/live/trade_history', methods=['GET', 'POST'])
def get_trade_history():
    #TODO: Fetch from trade history table  
    return 


@app_routes.route('/backtest/portfolio_data', methods=['GET', 'POST'])
def get_portfolio_data():
    symbols = request.args.getlist('symbol', type=str)
    portfolio = portfolio_value(symbols)
    return jsonify(portfolio)

@app_routes.route('/backtest/trade_history', methods=['GET', 'POST'])
def get_trade_data():
    symbols = request.args.getlist('symbol', type=str)
    trade_history = trades(symbols)
    return jsonify(trade_history)

@app_routes.route('/backtest/prediction_comparison', methods=['GET', 'POST'])
def prediction_comparison():
    symbol = request.args.get('symbol', type=str)
    predictions = compare_predictions(symbol)
    return jsonify(predictions)
