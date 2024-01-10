import React, { useEffect } from 'react';
import { useDispatch, useSelector } from 'react-redux';
import { getUserOrders } from '../../store/order';

function UserOrders() {
  const dispatch = useDispatch();
  const orders = useSelector(state => state.order.orders);

  useEffect(() => {
    dispatch(getUserOrders());
  }, [dispatch]);




  return (
    <div className="user-orders">
      <h2>Your Orders</h2>
      <table>
        <thead>
          <tr>
            <th>Order ID</th>
            <th>Total Price</th>
            <th>Order Date</th>
            <th>Delivery Address</th>
            <th>Status</th>
            <th>Created At</th>
            <th>Updated At</th>

          </tr>
        </thead>
        <tbody>
          {orders.map(order => (
            <tr key={order.id}>
              <td>{order.id}</td>
              <td>{order.total_price}</td>
              <td>{new Date(order.order_date).toLocaleDateString()}</td>
              <td>{order.delivery_address}</td>
              <td>{order.status}</td>
              <td>{new Date(order.created_at).toLocaleDateString()}</td>
              <td>{new Date(order.updated_at).toLocaleDateString()}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );

}

export default UserOrders;
