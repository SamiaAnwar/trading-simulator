from flask import Blueprint, request, jsonify
from app.backtesting import trades, portfolio_value, compare_predictions
from app.predictor import predict, trade_decision
from app.data_fetcher import get_live_data_features
from app.trade import portfolio_reset
import os
from supabase import create_client, Client

url: str = os.environ.get("SUPABASE_URL")
key: str = os.environ.get("SUPABASE_KEY")
supabase: Client = create_client(url, key)
user = os.environ.get("USER_ID")

app_routes = Blueprint('app_routes', __name__)

@app_routes.route('/live/scheduled_update', methods=['GET', 'PUT'])
def scheduled_update():
    #Get portfolio information 
    portfolio, _ = supabase.table("Portfolio").select("*").eq("user_id", user).execute()
    cash = portfolio[1][0]['cash']
    holdings = portfolio[1][0]['holdings_alt2']
    portfolio_reset(cash, holdings)
    #TODO: Make a decision
    #1) Get features from relevant stocks
    symbols = holdings.keys() #get symbols from holdings 
    features_data = get_live_data_features(symbols)
    #2) Make predictions and decisions from the feaatures 
    decisions = {}
    for symbol in symbols:
        prediction = predict(features_data[symbol].T)
        decisions[symbol] = trade_decision(prediction)
    #TODO: Update the databases (incl. PortfolioValues, Portfolio > holdings, Trades)
    #for symbol, decision in decisions:
        #if decision == 'BUY':
            #Execute buy logic 
        #if decision == 'SELL':
            #Execute buy logic 
    return jsonify(decisions)

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
