import React from 'react';

const ButtonSelector = ({ option, isSelected, toggleSelection }) => {
    return (
        <button
            className={`rounded-full px-4 py-2 m-2 ${isSelected ? "bg-blue-600 text-white" : "bg-gray-200 text-black"
                } hover: bg-blue-400 transition`}
            onClick={() => toggleSelection(option)}
        >
            {option}
        </button>
    );
};

export default ButtonSelector; 