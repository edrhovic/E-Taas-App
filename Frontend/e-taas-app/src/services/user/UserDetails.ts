import { userApi } from "../axios";


export const getUserDetails = async () => {
  try {
    const res = await userApi.get("/details/");
    console.log(res.data);
    return res.data;
  } catch (error) {
    console.error("Error fetching user details:", error);
    throw error;
  }
}