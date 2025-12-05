import { servicesApi } from "../axios/ApiServices";


export const getAllServices = async () => {
  try {
    const res = await servicesApi.get("/");
    return res.data;
  } catch (error) {
    console.error("Fetching all services failed:", error);
    throw error;
  }
};


export const getServiceById = async (serviceId: number) => {
  try {
    const res = await servicesApi.get(`/${serviceId}`);
    return res.data;
  } catch (error) {
    console.error(`Fetching service with ID ${serviceId} failed:`, error);
    throw error;
  }
};