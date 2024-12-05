import React from 'react';
import Chart from './Chart';
import './Dashboard.css';

const Dashboard = () => {
  return (
    <div className="dashboard">
      <h2>Dashboard</h2>
      <div className="charts-container">
        <Chart title="Log Levels Distribution" />
        <Chart title="Anomalies Detected" />
      </div>
    </div>
  );
};

export default Dashboard;
