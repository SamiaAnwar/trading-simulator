from flask import Blueprint, request, jsonify
from app.backtesting import trades, portfolio_value, compare_predictions
from app.predictor import predict, trade_decision
from app.data_fetcher import get_live_data_features
from app.trade import portfolio_reset, execute_trade, portfolio, calculate_portfolio_value
import os
from supabase import create_client, Client
from datetime import date


url: str = os.environ.get("SUPABASE_URL")
key: str = os.environ.get("SUPABASE_KEY")
supabase: Client = create_client(url, key)
user = os.environ.get("USER_ID")

app_routes = Blueprint('app_routes', __name__)

@app_routes.route('/live/scheduled_update', methods=['GET', 'PUT'])
def scheduled_update():
    #Get portfolio information 
    pf, _ = supabase.table("Portfolio").select("*").eq("user_id", user).execute()
    cash = pf[1][0]['cash']
    holdings = pf[1][0]['holdings_alt2']
    portfolio_reset(cash, holdings)
    #Get features from relevant stocks
    symbols = list(holdings.keys()) #get symbols from holdings 
    features_data = get_live_data_features(symbols)
    #Make predictions and decisions from the feaatures 
    decisions = {}
    live_prices = {}
    for symbol in symbols:
        prediction = predict(features_data[symbol].T)
        decisions[symbol] = trade_decision(prediction)
        live_prices[symbol] = [prediction['CURR_CLOSE']]
    #Execute the trade internally 
    today = str(date.today())
    for symbol, decision in decisions.items():
        action = -1 
        if decision == 'BUY':
            action = 1 
        if decision == 'SELL':
            action = 0 
        if action != -1 and (portfolio['stocks'][symbol] > 0 or action == 1): 
            #Add new trade to Trades
            response = (
                supabase.table("Trades")
                .insert(
                    {"user_id": user, 
                    "symbol": symbol, 
                    "date":today, 
                    "value":live_prices[symbol][0], 
                    "action": action}
                )
                .execute()
                )
        message = execute_trade(portfolio, symbol, decision, 1, live_prices[symbol][0])
    value = calculate_portfolio_value(portfolio, live_prices, 0)
    #Add new value to PortfolioValues 
    response = (
                supabase.table("PortfolioValues")
                .insert(
                    {"user_id": user,
                    "date":today, 
                    "value":value}
                )
                .execute()
                )
    #Update cash and holdings value 
    response = (
        supabase.table("Portfolio")
        .update({"cash": portfolio['cash'], "holdings":portfolio["stocks"]})
        .eq("user_id", user)
        .execute()
    )
    return jsonify(portfolio)

@app_routes.route('/live/portfolio', methods=['GET', 'POST'])
def get_live_portfolio():
    portfolio, _ = supabase.table("Portfolio").select("*").eq("user_id", user).execute()
    holdings = portfolio[1][0]['holdings']
    return holdings

@app_routes.route('/live/value_history', methods=['GET', 'POST'])
def get_value_history():
    values, _ = supabase.table("PortfolioValues").select("value, date").eq("user_id", user).execute()
    return jsonify(values[1])

@app_routes.route('/live/trade_history', methods=['GET', 'POST'])
def get_trade_history():
    trades, _ = supabase.table("Trades").select("symbol, date, value, action").eq("user_id", user).execute()
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
