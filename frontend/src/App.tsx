import { createResource } from "solid-js";
import { Table } from "./Table";

const ordersResource = createResource<any[]>("http://localhost:3000/orders");

export default function App() {
  const [orders] = ordersResource.read();

  return (
    <div class="p-4">
      <h1 class="text-2xl font-bold mb-4">Orders</h1>
      <Table data={orders} />
    </div>
  );
}
