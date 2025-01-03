from flask import Flask, request, jsonify
import pickle
import yfinance as yf
from alpaca_trade_api import REST
import pandas as pd