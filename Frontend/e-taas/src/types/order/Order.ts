export interface OrderData {
  shipping_address: string;
  payment_method: string;
  items: OrderItem[] | [{}];
}

export interface CartOrderData {
  shipping_address: string;
  payment_method: string;
  cart_items_id: number[];
}

interface OrderItem {
  product_id: number;
  variant_id?: number;
  quantity: number
}