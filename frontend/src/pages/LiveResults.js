import React, { useState, useEffect } from "react";
import LineGraph from "../components/LineGraph";
import DataTable from "../components/DataTable";
import DoughnutGraph from "../components/DoughnutGraph";
import axios from "axios";


const LiveResults=() => {
    const [valuesData, setValuesData] = useState([]);
    const [tradesData, setTradesData] = useState([]); 
    const [holdingsData, setHoldingsData] = useState([]);
    // const [selectedSym, setSelectedSym] = useState(Object.keys(holdingsData)[0] || "TSLA"); 
    // const [monthVals, setMonthVals] = useState([]); 
    axios.defaults.baseURL = 'https://trade-sim-flask-docker-339189756210.us-east1.run.app';

    useEffect(() => {
        axios.get('/live/value_history').then(
            response => (
                setValuesData(response.data)
            )
        ).catch(error => {
            console.error("Error fetching portfolio values data:", error);
        });
        axios.get('/live/trade_history').then(
            response => (
                setTradesData(response.data)
            )
        ).catch(error => {
            console.error("Error fetching trading data:", error);
        });
        axios.get('/live/portfolio').then(
            response => (
                setHoldingsData(response.data)
            )
        ).catch(error => {
            console.error("Error fetching holdings data:", error);
        }); 
    }, []); 

    // useEffect(() => {
    //     axios.get(`/live/daily_prices?symbol=${selectedSym}`).then(response => (
    //         setMonthVals(response.data)
    //     )).catch(error => {
    //         console.error("Error fetching daily prices of selected symbol:", error)
    //     })
    // }, [selectedSym]);

    // const dates = monthVals.map(item => new Date(item[1]).toLocaleDateString());
    // const prices = monthVals.map(item => item[0]);
    // console.log(dates)
    // const tradeDays = []
    // const tradeActions = []
    // for (let i = 0; i < tradesData.length; i++){
    //     if (tradesData[i]['symbol'] === selectedSym) {
    //         tradeDays.push(tradesData[i]['date']);
    //         tradeActions.push(tradesData[i]['action']);
    //     }
    // }
    // const tradeColors = pointColors(dates, tradeDays, tradeActions)
    // console.log(tradeColors)
    console.log(tradesData)
    const tradesTableData = tradesData.map(item => ({
        ...item,
        action: item.action === 1 ? "BUY" : "SELL"
      }));
    const lineData = Object.values(valuesData).map(({ date, value }) => [date, value]);
    const doughnutData = Object.entries(holdingsData); 
    
    return (
        <div className="min-h-screen bg-black p-6">
            <h1 className="text-3xl font-bold text-center text-white mb-8">
                Live Trading Simulator
            </h1>
            <div className="flex flex-row h-content space-x-4">
                <div className='min-h-full w-2/3  bg-black p-6 shadow-green rounded-lg object-cover border border-white'>
                    <h2 className=" text-xl font-semibold text-white mb-4"> Portfolio Value </h2>
                    <LineGraph data={lineData} />
                </div>
                <div className='min-h-full w-1/3  bg-black p-6 shadow-green rounded-lg object-cover border border-white'>
                    <div className="flex flex-row h-content justify-between">
                        <h2 className=" text-xl font-semibold text-white mb-4"> Holdings Distribution </h2>
                    </div>
                    <DoughnutGraph data={ doughnutData } />
                </div>
            </div>
            <div className='mt-6 bg-black p-6 shadow-white rounded-lg object-cover border border-white'>
                <DataTable data={tradesTableData} />
            </div>
        
        </div>
    );

}; 

export default LiveResults; 
