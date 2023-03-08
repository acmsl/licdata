import React from 'react';

interface TableProps {
    data: any[];
}

export function Table({ data }: TableProps) {
  return (
    <table className="w-full border-collapse">
      <thead>
        <tr>
          <th className="text-left font-bold p-2">#</th>
          <th className="text-left font-bold p-2">Client</th>
          <th className="text-left font-bold p-2">Product</th>
          <th className="text-left font-bold p-2">Duration</th>
          <th className="text-left font-bold p-2">Order Date</th>
        </tr>
      </thead>
      <tbody>
        {data.map((order, index) => (
            <tr className={`${index % 2 === 0 ? "bg-gray-100" : "bg-white"} hover:bg-gray-200 transition-colors`}
                key={order.id}>
                <td className="p-2">{index + 1}</td>
                <td className="p-2">{order.client_id}</td>
                <td className="p-2">{order.product_id}</td>
                <td className="p-2">{order.duration}</td>
                <td className="p-2">{order.order_date}</td>
            </tr>
        ))}
      </tbody>
    </table>
  );
}
