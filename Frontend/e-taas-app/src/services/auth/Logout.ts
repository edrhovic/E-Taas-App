import { userApi } from "../axios";


export const logoutUser = async () => {
  try {
    const res = await userApi.post("/logout");
    return res;
  } catch (error) {
    console.error("Error logging out:", error);
    throw error;
  }
}