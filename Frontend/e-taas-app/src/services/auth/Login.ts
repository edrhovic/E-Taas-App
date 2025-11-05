import { authApi } from "../axios"
import type { LoginData } from "../../types/Auth"

export const loginUser = async (credentials: LoginData) => {
  try {
    const response = await authApi.post("/login", credentials, { withCredentials: true });
    return response;
  }catch(e){
    console.log(e);
    throw new Error("Failed to login user.")
  }
}