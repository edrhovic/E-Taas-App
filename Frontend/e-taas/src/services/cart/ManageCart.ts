import { cartApi } from "../axios/ApiServices";
import type { AddCartData } from "../../types/cart/Cart";


export const addItemToCart = async (data: AddCartData) => {
  try {
    const res = await cartApi.post("/add-item", data);
    return res.data;
  } catch (error) {
    console.error("Adding item to cart failed:", error);
    throw error;
  }
};

export const updateCartItem = async (itemId: number, quantity: number) => {
  try {
    const res = await cartApi.put(`/update-item/${itemId}`, { quantity });
    return res.data;
  } catch (error) {
    console.error("Updating cart item failed:", error);
    throw error;
  }
};

export const removeItemFromCart = async (itemId: number) => {
  try {
    const res = await cartApi.delete(`/remove-item/${itemId}`);
    return res.data;
  } catch (error) {
    console.error("Removing item from cart failed:", error);
    throw error;
  }
};

export const clearCart = async () => {
  try {
    const res = await cartApi.delete("/clear");
    return res.data;
  } catch (error) {
    console.error("Clearing cart failed:", error);
    throw error;
  }
};