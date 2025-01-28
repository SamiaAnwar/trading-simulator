import React, { useState } from 'react';
import { useNavigate } from 'react-router';
import ButtonSelector from '../components/ButtonSelector';

const SymbolSelection = () => {
    const [selectedOptions, setSelectedOptions] = useState([]); 

    const tickers = { 'NVIDIA Corp.': "NVDA", 'Rigetti Computing Inc.': "RGTI", 'Rivian': "RIVN", 'Lucid Group Inc.': "LCID", 'Tesla Inc.': "TSLA", 'Apple Inc.': "AAPL", 'Ford Motor Co.': "F", 'Boeing Co.': "BA", 'Uber Technologies Inc': "UBER", 'First Solar Inc.': "FSLR", 'General Motors Co.': "GM", 'Micron Technology Inc.': "MU", 'Palantir Technologies Inc.': "PLTR", 'Walgreens Boots Alliance Inc.': "WBA", 'Moderna Inc.': "MRNA", 'Pfizer Inc.': "PFE", 'Estee Lauder Companies Inc.': "EL", 'Adobe Inc.': "ADBE", 'Alphabet Inc Class C (Google)': "GOOG", 'Amazon.com Inc': "AMZN", 'Microsoft Corp.': "MSFT" };
    
    const options = ['NVIDIA Corp.', 'Rigetti Computing Inc.', 'Rivian', 'Lucid Group Inc.', 'Tesla Inc.', 'Apple Inc.', 'Ford Motor Co.', 'Boeing Co.', 'Uber Technologies Inc', 'First Solar Inc.', 'General Motors Co.', 'Micron Technology Inc.', 'Palantir Technologies Inc.', 'Walgreens Boots Alliance Inc.', 'Moderna Inc.', 'Pfizer Inc.', 'Estee Lauder Companies Inc.', 'Adobe Inc.', 'Alphabet Inc Class C (Google)', 'Amazon.com Inc', 'Microsoft Corp.']; 
    const navigate = useNavigate();

    const toggleSelection = (option) => {
        option = tickers[option]; 
        setSelectedOptions((prevSelected) =>
            prevSelected.includes(option)
                ? prevSelected.filter((item) => item !== option)
                : [...prevSelected, option]
        );
    };

    const handleContinue = () => {
        navigate('/results', { state: { selectedOptions } });
    };

    return (
        <div className='flex flex-col items-center justify-center h-screen bg-black'>
            <h1 className='text-6xl text-white font-bold mb-4'> Create a Stock Portfolio </h1>
            <div className="flex flex-wrap justify-center w-3/5">
                {options.map((option) => (
                    <ButtonSelector
                        key={option}
                        option={option}
                        isSelected={selectedOptions.includes(tickers[option])}
                        toggleSelection={toggleSelection}
                    />
                ))}
            </div>
            <button
                className="mt-4 px-6 py-2 bg-pink-600 text-white rounded-full hover:bg-pink-500 transition"
                onClick={handleContinue}
                disabled={selectedOptions.length === 0}
            >
                Continue
            </button>
        </div>
    );
}; 

export default SymbolSelection; 