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
                label: "Portfolio Value",
                data: values,
                borderColor: "rgba(75,192,192,1)",
                backgroundColor: "rgba(75,192,192,0.2)",
                tension: 0.4,
            },
        ],
    }; 

    const options = {
        responsive: true,
        plugins: {
            legend: {
                display: true,
                position: 'top',
            },
        },
        scales: {
            x: {
                title: { display: true, text: "Date" },
            },
            y: {
                title: { display: true, text: "Value(USD)" },
            },
        },
    };
    return (
        <div style={{ marginBottom: '30px' }}>
            <h2> Portfolio Value </h2>
            <Line data={charData} options={options} />
        </div>
    ); 
}



export default LineGraph; 