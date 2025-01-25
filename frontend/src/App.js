import React, { useState, useEffect } from 'react'
import LineGraph from './components/LineGraph';
import DataTable from './components/DataTable';
import axios from "axios";

import './App.css';

function App() {
  const [portfolioData, setPortfolioData] = useState([]);
  const [tradeData, setTradeData] = useState([]);

  useEffect(() => {
    axios.get("/backtest/trade_history?symbol=AAPL&symbol=GOOG&symbol=UBER").then(response => (
      setTradeData(response.data)
    )).catch(error => {
      console.error("Error fetching portfolio data:", error);
    });
    axios.get("/backtest/portfolio_data?symbol=AAPL&symbol=GOOG&symbol=UBER").then(response => (
      setPortfolioData(response.data)
    )).catch(error => {
      console.error("Error fetching portfolio data:", error);
    });

  }, [])
  return (
    <div className="min-h-screen bg-gray-100 p-6">
      <h1 className="text-3xl font-bold text-center text-blue-500 mb-8">
        Stock Market Predictor
      </h1>
      <div className='bg-white p-6 shadow-lg rounded-lg'>
        <LineGraph data={portfolioData} />
      </div>
      <div className='mt-6 bg-white p-6 shadow-lg rounded-lg'>
        <DataTable data={tradeData} />
      </div>
    </div>
  );
}

export default App;
