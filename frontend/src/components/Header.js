import React from 'react';
import './Header.css';

const Header = () => {
  return (
    <header className="header">
      <h1>Log190 SIEM Tool</h1>
      <nav>
        <a href="/">Dashboard</a>
        <a href="/logs">Logs</a>
      </nav>
    </header>
  );
};

export default Header;
