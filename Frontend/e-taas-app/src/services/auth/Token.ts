import { authApi } from "../axios";


export const refreshUserToken = async () => {
  try {
    const res = await authApi.post("/token/refresh", {}, { withCredentials: true });
    console.log(res);
    return res;
  }catch (e) {
    console.log(e);
    throw new Error("Failed to refresh token.");
  }
};
