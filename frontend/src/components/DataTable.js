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
            <h2 className="text-xl font-semibold text-gray-700 mb-4"> Trade Action</h2>
            <div className="overflow-x-auto">
                <table
                    {...getTableProps()} style={{ border: "1px solid black", width: "100%" }}
                    className="min-w-full table-auto border-collapse border border-gray-300"
                >
                    <thead className="bg-gray-100">
                        {headerGroups.map(headerGroup => (
                            <tr {...headerGroup.getHeaderGroupProps()}>
                                {headerGroup.headers.map(column => (
                                    <th
                                        {...column.getHeaderProps()}
                                        style={{ border: "1px solid black", padding: "8px" }}
                                        className="border border-gray-300 px-4 py-2 text-left text-sm font-medium text-gray-600"
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
                                    className="hover:bg-gray-50"
                                >
                                    {row.cells.map(cell => (
                                        <td
                                            {...cell.getCellProps()}
                                            style={{ border: "1px solid black", padding: "8px" }}
                                            className="border border-gray-300 px-4 py-2 text-sm text-gray-700"
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
