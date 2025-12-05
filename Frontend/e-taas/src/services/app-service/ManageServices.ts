import { servicesApi } from "../axios/ApiServices";
import type { ServiceData } from "../../types/app-services/Services";


export const addService = async (data: ServiceData) => {
  try {
    const res = await servicesApi.post("/add-service", data);
    return res.data;
  } catch (error) {
    console.error("Adding new service failed:", error);
    throw error;
  } 
};


export const addImageToService = async (serviceId: number, images: FormData) => {
  try {
    const res = await servicesApi.post(`/add-service-images/${serviceId}`, images);
    return res.data;
  } catch (error) {
    console.error("Adding images to service failed:", error);
    throw error;
  }
};