from flask import Blueprint, request, jsonify
import json
from app.data_fetcher import get_live_data

app_routes = Blueprint('app_routes', __name__)

@app_routes.route("/get_live_data", methods=['GET', 'POST'])
def live_data():
    symbols = request.args.getlist('symbol', type=str)
    data = get_live_data(symbols)
    data_json = json.dumps(data, indent=4)
    return data_json