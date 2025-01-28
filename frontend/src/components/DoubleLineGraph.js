import React from "react";
import { Line } from "react-chartjs-2";
import {
  Chart as ChartJS,
  CategoryScale,
  LinearScale,
  PointElement,
  LineElement,
  Title,
  Tooltip,
  Legend,
} from "chart.js";

// Register necessary chart.js components
ChartJS.register(CategoryScale, LinearScale, PointElement, LineElement, Title, Tooltip, Legend);

const DoubleLineGraph = ({ data }) => {
  // Process data into labels and datasets
  const labels = data.map((item) => new Date(item[0]).toLocaleDateString("en-US"));

  const line1Data = data.map((item) => item[1]); // First line (e.g., actual price)
  const line2Data = data.map((item) => item[2]); // Second line (e.g., predicted price)

  const chartData = {
    labels, // Dates for the x-axis
    datasets: [
      {
        label: "Actual Price", // First line label
        data: line1Data, // Y-axis data for the first line
        borderColor: "rgb(75, 192, 192)",
        backgroundColor: "rgba(75, 192, 192, 0.2)",
        tension: 0.3, // Curve smoothness
      },
      {
        label: "Predicted Price", // Second line label
        data: line2Data, // Y-axis data for the second line
        borderColor: "rgb(255, 99, 132)",
        backgroundColor: "rgba(255, 99, 132, 0.2)",
        tension: 0.3, // Curve smoothness
      },
    ],
  };

  const options = {
    responsive: true,
    plugins: {
      legend: {
        position: "top", // Legend position
      },
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
          title: { display: true, text: "Price (USD)", color: 'white' },
          grid: { color: 'white' },
          labels: { color: 'white' },
          ticks: {color: 'rgb(159, 159, 159)'},
          
      },
    },
  };

  return (
        <div className="relative object-cover resize">
            <Line data={chartData} options={options} />
        </div>
    ); 
};

export default DoubleLineGraph;
