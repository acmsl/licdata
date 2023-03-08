import React from 'react';
import { render, screen } from '@testing-library/react';
import { extendExpect } from '@testing-library/jest-dom/extend-expect';

import { Table } from "./Table";

describe("Table component", () => {
  it("renders the table headers", () => {
    const { getByText } = render(<Table data={[]} />);

    expect(getByText("#")).toBeInTheDocument();
    expect(getByText("Client")).toBeInTheDocument();
    expect(getByText("Product")).toBeInTheDocument();
    expect(getByText("Duration")).toBeInTheDocument();
    expect(getByText("Order Date")).toBeInTheDocument();
  });

  it("renders the orders data", () => {
    const data = [
        {
            id: "1",
            client_id: "client-1",
            product_id: "product-1",
            duration: "1 year",
            order_date: "2023-03-08",
        },
        {
            id: "2",
            client_id: "client-2",
            product_id: "product-2",
            duration: "6 months",
            order_date: "2023-03-07",
        },
    ];
    const { getByText } = render(<Table data={data} />);

    expect(getByText("client-1")).toBeInTheDocument();
    expect(getByText("product-1")).toBeInTheDocument();
    expect(getByText("1 year")).toBeInTheDocument();
    expect(getByText("2023-03-08")).toBeInTheDocument();

    expect(getByText("client-2")).toBeInTheDocument();
    expect(getByText("product-2")).toBeInTheDocument();
    expect(getByText("6 months")).toBeInTheDocument();
    expect(getByText("2023-03-07")).toBeInTheDocument();
  });
});
