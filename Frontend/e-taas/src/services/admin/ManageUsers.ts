import { adminApi } from "../axios/ApiServices";

export const getAllUsers = async () => {
  try {
    const res = await adminApi.get("/users");
    return res.data;
  } catch (error) {
    console.error("Fetching all users failed:", error);
    throw error;
  }
};

export const getSellers = async () => {
  try {
    const res = await adminApi.get("/sellers");
    return res.data;
  } catch (error) {
    console.error("Fetching sellers failed:", error);
    throw error;
  }
};
