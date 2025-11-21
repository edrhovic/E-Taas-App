import { authApi } from "../axios"
import type { LoginData } from "../../types/Auth"
import type { RegisterData, VerifyRegistration } from "../../types/Auth";


export const registerUser = async (registerData: RegisterData) => {
  try {
    const res = await authApi.post("/register", registerData);
    return res;
  }catch(e){
    console.log(e);
    throw new Error("Failed to register user.")
  }
}

export const verifyOtp = async (verifyData: VerifyRegistration) => {
  try {
    const res = await authApi.post("/verify-email-otp", verifyData);
    return res;
  }catch(e){
    console.log(e);
    throw new Error("Failed to verify OTP.")
  }
}

export const loginUser = async (credentials: LoginData) => {
  try {
    const response = await authApi.post("/login", credentials, { withCredentials: true });
    return response;
  }catch(e){
    console.log(e);
    throw new Error("Failed to login user.")
  }
}

