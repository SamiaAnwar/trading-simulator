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
            <h2> Trade Action</h2>
            <table {...getTableProps()} style={{ border: "1px solid black", width: "100%" }}>
                <thead>
                    {headerGroups.map(headerGroup => (
                        <tr {...headerGroup.getHeaderGroupProps()}>
                            {headerGroup.headers.map(column => (
                                <th
                                    {...column.getHeaderProps()}
                                    style={{ border: "1px solid black", padding: "8px" }}
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
                            <tr {...row.getRowProps()} >
                                {row.cells.map(cell => (
                                    <td
                                        {...cell.getCellProps()}
                                        style={{ border: "1px solid black", padding: "8px" }}
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
    );
}; 
export default DataTable; 
