import React from 'react';
import { Bar } from 'react-chartjs-2';

const Barchart = ({ data}) => {
    const chartData = ({ data }) => {
        labels: data.map(item => item.label),
        datasets: [
            {
                label: 'Usage Data',
                data: data.map(item => item.value),
                backgroudColor: 'rgba(75, 192, 192, 0.2)',
                borderColor: 'rgba(75, 192, 192, 1)',
                borderWidth: 1,
            },
        ],
    };

    const options = {
        responsive: true,
        scales: {
            y: {
                beginAtZero: true,
            },
        },
    };
    return <Bar data={chartData} options={options} />;
};

export default Barchart;