import { adminApi } from "../axios/ApiServices";

export const addProductCategory = async (category_name: string) => {
  try {
    const res = await adminApi.post("/add-product-category", { category_name });
    return res.data;
  } catch (error) {
    console.error("Adding product category failed:", error);
    throw error;
  }
};

export const addServiceCategory = async (name: string) => {
  try {
    const res = await adminApi.post("/add-service-category", { name });
    return res.data;
  } catch (error) {
    console.error("Adding service category failed:", error);
    throw error;
  }
};