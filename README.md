# stock-market-predictor
## Objective
The objective of this project is to create a tool which can aid in demystifying the statistical element of stock market prices to make trading more accessible to the average earner. 

## About 
This tool leverages historical data from 21 different tickers and simulates trading actions over a one-month period based on a machine learning model. It allows the user to choose the tickers on which they want to trade and visualizes the profits made from these trades over the course of the subsequent month, using real daily closing values from the yfinance library. It also visualizes the model accuracy of the model’s 30-day projections vs. the actual price 30 trading days in the future. 

## Tools 
This application uses create-react-app, TailwindCSS with react-chart-js2 for its data visualisation. The API endpoints to query the data and obtain the stock market data and trading simulation were written in Flask and Python. The model was generated using Python scripts, using a Random Forest Regressor from scikit-learn and processed using Pandas dataframes. 

All the stock market data for training and testing the model and for visualising results are from the yfinance library.

## Demo 

https://github.com/user-attachments/assets/df130842-16a0-4c48-8d46-9e666e9f6f83


## Installation 
```sh
$ cd frontend && npm i
```
