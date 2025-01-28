import React, { useState } from "react"; 

const DropDown = ({ options, onSelect }) => {
    const [selectedItem, setSelectedItem] = useState(options[0] || "");
    function handleChange( event ) {
        setSelectedItem(event.target.value);
        onSelect(selectedItem)
    };
    return (
            
            <select
                id="dropdown"
                value={selectedItem}
                onChange={handleChange}
                className="block w-1/4 bg-gray-900 border border-gray-300 rounded-md shadow-sm px-4 py-2 focus:outline-none focus:ring focus:ring-indigo-500 focus:border-indigo-500 text-white"
            >
                {options.map((option, index) => (
                    <option key={index} value={option}>
                        {option}
                    </option>
                ))}
            </select>
    
    );

};

export default DropDown; 