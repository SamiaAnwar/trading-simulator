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

  })
  return (
    <div style={{ padding: "20px" }}>
      <h1>Stock Market Predictor</h1>
      <LineGraph data={portfolioData} />
      <DataTable data={tradeData} />
    </div>
  );
}

export default App;
