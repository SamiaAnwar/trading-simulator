import React, { useState, useEffect } from "react"; 
import { useLocation } from "react-router"; 
import LineGraph from "../components/LineGraph";
import DataTable from "../components/DataTable";
import DoubleLineGraph from "../components/DoubleLineGraph";
import DropDown from "../components/DropDown";
import axios from "axios";

const TradingResults = () => {
  const location = useLocation(); 
  const { selectedOptions } = location.state || { selectedOptions: [] };
  const query = selectedOptions.join("&symbol=")
  const [selectedSym, setSelectedSym] = useState(selectedOptions[0] || ""); 
  const [tradeData, setTradeData] = useState([]);
  const [portfolioData, setPortfolioData] = useState([]);
  const [compareData, setCompareData] = useState([]); 

  function handleSelect(symbol){
    setSelectedSym(symbol);
  };  

  axios.defaults.baseURL = 'https://flask-docker-339189756210.us-east1.run.app';
  useEffect(() => {
      axios.get(`/backtest/trade_history?symbol=${query}`).then(response => (
          setTradeData(response.data)
      )).catch(error => {
          console.error("Error fetching trading data:", error);
      });
  }, []); 

  useEffect(() => {
    axios.get(`/backtest/portfolio_data?symbol=${query}`).then(response => (
      setPortfolioData(response.data)
    )).catch(error => {
      console.error("Error fetching portfolio data:", error);
    });
  }, [tradeData]);
  
  useEffect(() => {
    axios.get(`/backtest/prediction_comparison?symbol=${selectedSym}`).then(response => (
      setCompareData(response.data)
    )).catch(error => {
      console.error("Error fetching symbol:", error);
    });
  }, [selectedSym]);
  return (
      <div className="min-h-screen bg-gray-900 p-6">
        <h1 className="text-3xl font-bold text-center text-white mb-8">
          Backtesting Results
        </h1>
        <div className="flex flex-row h-content space-x-4">
          <div className='min-h-full w-1/2  bg-gray-900 p-6 shadow-green rounded-lg object-cover border border-white'>
            <h2 className=" text-xl font-semibold text-white mb-4"> Portfolio Value </h2>
            <LineGraph data={portfolioData} />
          </div>
          <div className='min-h-full w-1/2  bg-gray-900 p-6 shadow-green rounded-lg object-cover border border-white'>
            <div className="flex flex-row h-content justify-between">
              <h2 className=" text-xl font-semibold text-white mb-4"> Model Accuracy </h2>
              <DropDown options={selectedOptions} onSelect={handleSelect} />
            </div>
            <DoubleLineGraph data={compareData} />
          </div>
        </div>
      
        <div className='mt-6 bg-gray-900 p-6 shadow-white rounded-lg object-cover border border-white'>
          <DataTable data={tradeData} />
        </div>
      </div>
  );
}; 

export default TradingResults; 
