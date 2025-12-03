interface ProductData {
  product_name: string;
  description: string;
  base_price: number;
  stock: number;
  has_variants: boolean;
  category_id: number;
  variant_categories?: VariantCategory[];
  variants?: VariantData[];
}

interface VariantData {
  stock: number;
  price: number;
}

interface VariantCategory{
  category_name: string;
  attributes: VariantAttribute[];
}

interface VariantAttribute {
  value: string;
}

export interface AddProductRequest {
  data: ProductData;
  product_images: File[];
}