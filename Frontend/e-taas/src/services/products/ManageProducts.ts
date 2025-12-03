import { productApi } from "../axios/ApiServices";
import type { AddProductRequest } from "../../types/products/Products";

export const addProduct = async (data: AddProductRequest) => {
  try {
    const res = await productApi.post("/add-product", data);
    return res.data;
  } catch (error) {
    console.error("Adding product failed:", error);
    throw error;
  }
};