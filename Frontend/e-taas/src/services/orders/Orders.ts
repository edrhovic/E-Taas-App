import { orderApi } from "../axios/ApiServices";


export const getUserOrders = async () => {
  try {
    const res = await orderApi.get("/");
    return res.data;
  } catch (error) {
    console.error("Fetching user orders failed:", error);
    throw error;
  }
};

export const getOrderById = async (orderId: number) => {
  try {
    const res = await orderApi.get(`/${orderId}`);
    return res.data;
  } catch (error) {
    console.error("Fetching order by ID failed:", error);
    throw error;
  }
};