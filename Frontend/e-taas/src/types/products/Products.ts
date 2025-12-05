interface ProductData {
  product_name: string;
  description: string;
  base_price: number;
  stock: number;
  has_variants: boolean;
  category_id: number;
  seller_id: number;
  variant_categories?: VariantCategory[];
  variants?: VariantData[];
}

interface VariantData {
  stock: number;
  price: number;
}


interface VariantAttribute {
  value: string;
}

interface VariantCategory{
  category_name: string;
  attributes: VariantAttribute[];
}


export interface AddProductRequest {
  product: ProductData;
}
