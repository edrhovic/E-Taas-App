import { orderApi } from "../axios/ApiServices";
import type { OrderData, CartOrderData } from "../../types/order/Order";



export const checkoutOrder = async (data: OrderData) => {
  try {
    const res = await orderApi.post("/checkout", data);
    return res.data;
  } catch (error) {
    console.error("Creating order failed:", error);
    throw error;
  }
};

export const checkoutOrderFromCart = async (data: CartOrderData) => {
  try {
    const res = await orderApi.post("/checkout-cart", data);
    return res.data;
  } catch (error) {
    console.error("Creating order from cart failed:", error);
    throw error;
  }
};


export const cancelOrder = async (orderId: number) => {
  try {
    const res = await orderApi.post(`/cancel/${orderId}`);
    return res.data;
  } catch (error) {
    console.error("Cancelling order failed:", error);
    throw error;
  }
};


export const markOrderAsReceived = async (orderId: number) => {
  try {
    const res = await orderApi.post(`/mark-received/${orderId}`);
    return res.data;
  } catch (error) {
    console.error("Marking order as received failed:", error);
    throw error;
  }
};