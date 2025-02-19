import React, { useState, useEffect, use } from "react"; 
import { useLocation } from "react-router"; 
import LineGraph from "../components/LineGraph";
import DataTable from "../components/DataTable";
import axios from "axios";


const LiveResults=() => {
    const [valuesData, setValuesData] = useState([]);
    const [tradesData, setTradesData] = useState([]); 
    useEffect(() => {
        axios.get('/live/value_history').then(
            response => (
                setValuesData(response.data)
            )
        ).catch(error => {
            console.error("Error fetching portfolio values data:", error);
        })
    }, [])

    useEffect(() => {
        axios.get('/live/trade_history').then(
            response => (
                setTradesData(response.data)
            )
        ).catch(error => {
            console.error("Error fetching portfolio values data:", error);
        })
    }, [])
    const tradesTableData = tradesData.map(item => ({
        ...item,
        action: item.action === 1 ? "BUY" : "SELL"
      }));
      
    const lineData = Object.values(valuesData).map(({ date, value }) => [date, value]);
    
    console.log(tradesData)
    return (
        <div className="min-h-screen bg-gray-900 p-6">
            <h1 className="text-3xl font-bold text-center text-white mb-8">
                Live Trading Simulator
            </h1>
            <div className="flex flex-row h-content space-x-4">
                <div className='min-h-full w-1/2  bg-gray-900 p-6 shadow-green rounded-lg object-cover border border-white'>
                    <h2 className=" text-xl font-semibold text-white mb-4"> Portfolio Value </h2>
                    <LineGraph data={lineData} />
                </div>
            </div>
            <div className='mt-6 bg-gray-900 p-6 shadow-white rounded-lg object-cover border border-white'>
                <DataTable data={tradesTableData} />
            </div>
        
        </div>
    );

}; 

export default LiveResults; 
