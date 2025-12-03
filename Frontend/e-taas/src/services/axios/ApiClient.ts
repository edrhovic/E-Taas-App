import type { AxiosInstance } from "axios";

export const createApiClient = (axiosInstance: AxiosInstance) => {
  return {
    get: <T = any> (url: String, config = {}) => axiosInstance.get<T>(url as string, config),
    post: <T = any> (url: String, data?: any, config = {}) => axiosInstance.post<T>(url as string, data, config),
    put: <T = any> (url: String, data?: any, config = {}) => axiosInstance.put<T>(url as string, data, config),
    delete: <T = any> (url: String, config = {}) => axiosInstance.delete<T>(url as string, config),
  };
}