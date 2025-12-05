import { getAllProducts } from "../../../services/products/Products";
import { useEffect } from "react";
import { addProduct } from "../../../services/products/ManageProducts";
import type { AddProductRequest } from "../../../types/products/Products";

export const Products: React.FC = () => {

  const newProduct: AddProductRequest = {
    product: {
    product_name: "Men's Oversized T-Shirt",
    description: "High-quality cotton oversized shirt available in multiple colors and sizes.",
    base_price: 350,
    stock: 100,
    has_variants: true,
    category_id: 1,
    seller_id: 1,

    variant_categories: [
      {
        category_name: "Color",
        attributes: [
          { value: "Black" },
          { value: "White" },
          { value: "Olive Green" }
        ]
      },
      {
        category_name: "Size",
        attributes: [
          { value: "Small" },
          { value: "Medium" },
          { value: "Large" },
          { value: "XL" }
        ]
      }
    ],
      variants: [{
        stock: 20,
        price: 350
      }]
    },
    product_images: []
  };

  useEffect(() => {
    const addNewProduct = async () => {
      try {
        console.log("Adding product:", newProduct);
        const products = await addProduct(newProduct);
        console.log("Added product:", products);
      } catch (error) {
        console.error("Error adding product:", error);
      }
    };

    addNewProduct();
  }, []);
  return (
    <>
      <div className="text-3xl">Products Page</div>
    </>
  );
}
