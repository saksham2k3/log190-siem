import React from 'react';
import { Bar } from 'react-chartjs-2';
import './Chart.css';

const Chart = ({ title }) => {
  const data = {
    labels: ['Info', 'Warning', 'Error'],
    datasets: [
      {
        label: 'Log Levels',
        data: [10, 5, 2],
        backgroundColor: ['#36a2eb', '#ffcd56', '#ff6384'],
      },
    ],
  };

  return (
    <div className="chart">
      <h3>{title}</h3>
      <Bar data={data} />
    </div>
  );
};

export default Chart;
