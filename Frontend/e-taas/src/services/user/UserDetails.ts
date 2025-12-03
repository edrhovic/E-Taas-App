import { userApi } from "../axios/ApiServices";

export const getUserDetails = async () => {
  try {
    const response = await userApi.get("/details");
    return response.data;
  } catch (error) {
    console.error("Fetching user details failed:", error);
    throw error;
  }
}