import axios from "axios";
import { refreshUserToken } from "../services/auth/Token";

export const authApi = axios.create({
  baseURL: "http://127.0.0.1:8000/v1/api/auth/",
  headers: {
    "Content-Type" : "application/json"
  }
});

export const userApi = axios.create({
  baseURL: "http://127.0.0.1:8000/v1/api/users/",
  headers: {
    "Content-Type" : "application/json"
  },
  withCredentials: true,
});


userApi.interceptors.response.use(
  (response) => {
    return response;
  },
  async (error) => {
    const originalRequest = error.config;
    if (error.response.status === 401 && !originalRequest._retry) {
      originalRequest._retry = true;
      try {
        await refreshUserToken();
        return userApi(originalRequest);
      } catch (e) {
        return Promise.reject(e);
      }
    }
    return Promise.reject(error);
  }
);