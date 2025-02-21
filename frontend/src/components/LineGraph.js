import React from "react"; 
import { Line } from "react-chartjs-2"; 
import {
    Chart as CharJS,
    CategoryScale,
    LinearScale,
    PointElement,
    LineElement,
    Title,
    Tooltip,
    Legend,
} from "chart.js";

CharJS.register(CategoryScale, LinearScale, PointElement, LineElement, Title, Tooltip, Legend); 

const LineGraph = ({ data }) => {
    const labels = data.map(item => new Date(item[0]).toLocaleDateString());
    const values = data.map(item => item[1])

    const charData = {
        labels,
        datasets: [
            {
                data: values,
                borderColor: "lime",
                backgroundColor: "rgba(75,192,192,0.2)",
                tension: 0.4,
            },
        ],
    }; 

    const options = {
        responsive: true,
        plugins: {
            legend: {
                display: false,
                position: 'top',
                color: 'white'
            }
        },
        scales: {
            x: {
                display: true,
                title: { display: true, text: "Date", color: 'white' },
                grid: { color: 'white' },
                ticks: {color: 'rgb(159, 159, 159)'},
            },
            y: {
                color: 'white',
                display: true,
                title: { display: true, text: "Value(USD)", color: 'white' },
                grid: { color: 'white' },
                labels: { color: 'white' },
                ticks: {color: 'rgb(159, 159, 159)'},
                
            },
        },
    };
    return (
        
        <div className="relative object-cover resize">
            <Line data={charData} options={options} />
        </div>
    
    ); 
}



export default LineGraph; 