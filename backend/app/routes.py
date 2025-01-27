from flask import Blueprint, request, jsonify
import json
from app.data_fetcher import get_live_data
from app.predictor import predict, trade_decision
from app.backtesting import trades, portfolio_value, compare_predictions
app_routes = Blueprint('app_routes', __name__)


@app_routes.route("/get_live_data", methods=['GET', 'POST'])
def live_data():
    symbols = request.args.getlist('symbol', type=str)
    data = get_live_data(symbols)
    data_json = json.dumps(data, indent=4)
    return data_json

@app_routes.route('/predict', methods=['GET', 'POST'])
def make_prediction():
    data = request.json()
    print(data)
    model_input = json.loads(data)
    prediction = predict(model_input)
    decision = trade_decision(prediction)
    return jsonify(decision)

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
