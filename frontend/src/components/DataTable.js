import React from "react";
import { useTable } from "react-table"; 

const DataTable = ({ data }) => {
    const columns = React.useMemo(
        () => [
            { Header: "Symbol", accessor: 'symbol' },
            { Header: "Action", accessor: 'action' },
            { Header: "Price", accessor: 'price' },
            { Header: "Date", accessor: 'date' },
        ],
        []
    );
    for (var i = 0; i < data.length; i++) {
        data[i].date = new Date(data[i].date).toLocaleDateString();
        data[i].price = Math.round(data[i].price * 1000) / 1000;
    }
    const tableInstance = useTable({ columns, data });

    const {
        getTableProps,
        getTableBodyProps,
        headerGroups,
        rows,
        prepareRow,
    } = tableInstance;

    return (
        <div>
            <h2 className="text-xl font-semibold text-white mb-4"> Trading History</h2>
            <div className="overflow-x-auto">
                <table
                    {...getTableProps()} style={{ border: "1px solid black", width: "100%" }}
                    className="min-w-full table-auto border-collapse border border-gray-300 rounded-sm"
                >
                    <thead className="bg-gray-700">
                        {headerGroups.map(headerGroup => (
                            <tr {...headerGroup.getHeaderGroupProps()}>
                                {headerGroup.headers.map(column => (
                                    <th
                                        {...column.getHeaderProps()}
                                        style={{ border: "1px solid gray", padding: "8px" }}
                                        className="border border-gray-300 px-4 py-2 text-left text-sm font-medium text-white"
                                    >
                                        {column.render("Header")}
                                    </th>
                                ))}
                            </tr>
                        ))}
                    </thead>
                    <tbody {...getTableBodyProps()}>
                        {rows.map(row => {
                            prepareRow(row);
                            return (
                                <tr
                                    {...row.getRowProps()}
                                    className="hover:bg-gray-500"
                                >
                                    {row.cells.map(cell => (
                                        <td
                                            {...cell.getCellProps()}
                                            style={{ border: "1px solid gray", padding: "8px" }}
                                            className="border border-gray-300 px-4 py-2 text-sm text-white"
                                        >
                                            {cell.render("Cell")}
                                        </td>
                                    ))}
                                </tr>
                            );
                        })}
                    </tbody>
                </table>
            </div>
        </div>
    );
}; 
export default DataTable; 
