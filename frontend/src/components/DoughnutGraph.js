import React from "react";
import { Chart as ChartJS, ArcElement, Tooltip, plugins, Legend} from 'chart.js';
import { Doughnut } from 'react-chartjs-2';

//Registering necessary chart.js components
ChartJS.register(ArcElement, Tooltip, Legend, plugins);

const DoughnutGraph = ({ data }) => {
    const labels = data.map((item) => item[0]);
    const count = data.map((item) => item[1]);
    const colors = []; 
    for (let i = 0; i < count.length; i++){
        const randomColor = "#" + Math.floor(Math.random() * 16777215).toString(16);
        colors.push(randomColor);
    };
    const chartData = {
        labels, 
        datasets: [
            {
                label: "Number of Stocks", 
                data: count,
                backgroundColor: colors
            }
        ]
    }; 
    const options = {
        plugins: {
            legend: {
                position: 'right'
            }
        }
    }; 

    return (
        <div className="relative resize">
            <Doughnut data={ chartData } options={ options } />
        </div>
    )

};

export default DoughnutGraph; 