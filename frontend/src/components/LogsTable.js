import React, { useEffect, useState } from 'react';
import './LogsTable.css';

const LogsTable = () => {
  const [logs, setLogs] = useState([]);

  useEffect(() => {
    fetch('/api/logs')
      .then((res) => res.json())
      .then((data) => setLogs(data))
      .catch((err) => console.error(err));
  }, []);

  return (
    <div className="logs-table">
      <h2>Logs</h2>
      <table>
        <thead>
          <tr>
            <th>Timestamp</th>
            <th>Log Level</th>
            <th>Message</th>
          </tr>
        </thead>
        <tbody>
          {logs.map((log, index) => (
            <tr key={index}>
              <td>{log[1]}</td>
              <td>{log[2]}</td>
              <td>{log[3]}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
};

export default LogsTable;
