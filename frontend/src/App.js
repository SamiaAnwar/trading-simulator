import React from 'react'; 
import { BrowserRouter as Router, Routes, Route } from "react-router"; 
import SymbolSelection from './pages/SymbolSelection';
import TradingResults from './pages/TradingResults';
import LiveResults from './pages/LiveResults';

import './App.css';

const App = () => {
  return (
    <Router>
      <Routes>
        <Route path="/" element={<SymbolSelection />} />
        <Route path="/backtesting" element={<TradingResults />} />
        <Route path="/live" element={<LiveResults/>} />

      </Routes>
    </Router>
  ); 
}; 
export default App;
