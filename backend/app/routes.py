from flask import Blueprint, request, jsonify
from app.backtesting import trades, portfolio_value, compare_predictions
import os
from supabase import create_client, Client

url: str = os.environ.get("SUPABASE_URL")
key: str = os.environ.get("SUPABASE_KEY")
supabase: Client = create_client(url, key)
user = os.environ.get("USER_ID")
user = 1

app_routes = Blueprint('app_routes', __name__)

@app_routes.route('/live/scheduled_update', methods=['GET', 'PUT'])
def scheduled_update():
    portfolio, _ = supabase.table("Portfolio").select("*").eq("user_id", user).execute()
    cash = portfolio[1][0]['cash']
    holdings = portfolio[1][0]['holdings']
    portfolio_reset(cash, holdings)
    #TODO: Make a decision

    #TODO: Update the databases (incl. PortfolioValues, Portfolio > holdings, Trades)
    
    return {'Hello':cash}

@app_routes.route('/live/portfolio', methods=['GET', 'POST'])
def get_live_portfolio():
    #TODO: Fetch from portfolio table   
    portfolio, _ = supabase.table("Portfolio").select("*").eq("user_id", user).execute()
    holdings = portfolio[1][0]['holdings']
    return holdings

@app_routes.route('/live/value_history', methods=['GET', 'POST'])
def get_value_history():
    #TODO: Fetch from value history table  
    values, _ = supabase.table("PortfolioValues").select("value, date").eq("user_id", user).execute()
    return jsonify(values[1])

@app_routes.route('/live/trade_history', methods=['GET', 'POST'])
def get_trade_history():
    #TODO: Fetch from trade history table  
    trades, _ = supabase.table("Trades").select("ticker, date, value").eq("user_id", user).execute()
    return jsonify(trades[1])

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
