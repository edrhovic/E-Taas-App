import { adminApi } from "../axios/ApiServices";


export const getAllApplications = async () => {
  try {
    const res = await adminApi.get("/seller-applications");
    return res.data;
  } catch (error) {
    console.error("Fetching all applications failed:", error);
    throw error;
  }
};

export const approveSellerApplication = async (sellerId: number) => {
  try {
    const res = await adminApi.post("/verify-seller", { sellerId });
    return res.data;
  } catch (error) {
    console.error("Approving seller application failed:", error);
    throw error;
  }
};