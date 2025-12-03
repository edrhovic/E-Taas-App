import { createApiClient } from "./ApiClient";
import { createApiInstance } from "./AxiosInstance";

const API_URL = import.meta.env.VITE_API_URL

export const authApi = createApiClient(createApiInstance(`${API_URL}/v1/api/auth`))
export const userApi = createApiClient(createApiInstance(`${API_URL}/v1/api/users`, true))
export const sellerApi = createApiClient(createApiInstance(`${API_URL}/v1/api/sellers`, true))
export const productApi = createApiClient(createApiInstance(`${API_URL}/v1/api/products`))
export const servicesApi = createApiClient(createApiInstance(`${API_URL}/v1/api/services`, true))
export const cartApi = createApiClient(createApiInstance(`${API_URL}/v1/api/cart`, true))
export const orderApi = createApiClient(createApiInstance(`${API_URL}/v1/api/orders`, true))
export const chatApi = createApiClient(createApiInstance(`${API_URL}/v1/api/chats`, true))
export const conversationApi = createApiClient(createApiInstance(`${API_URL}/v1/api/conversations`, true))
export const notificationApi = createApiClient(createApiInstance(`${API_URL}/v1/api/notifications`, true))
export const adminApi = createApiClient(createApiInstance(`${API_URL}/v1/api/admin`, true))