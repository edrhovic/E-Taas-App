import { cartApi } from "../axios/ApiServices";


export const getCartItems = async () => {
  try {
    const res = await cartApi.get("/");
    return res.data;
  } catch (error) {
    console.error("Fetching cart items failed:", error);
    throw error;
  }
};

