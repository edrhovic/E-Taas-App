from fastapi import HTTPException, status
from fastapi.responses import JSONResponse
from models.products import Product
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from schemas.product import ProductCreate, ProductUpdate

async def add_product(db: AsyncSession, product: ProductCreate, seller_id: int) -> JSONResponse:
    try:
        new_product = Product(
            product_name=product.product_name,
            description=product.description,
            base_price=product.base_price,
            stock=product.stock,
            has_variants=product.has_variants,
            category_id=product.category_id,
            seller_id=seller_id
        )
        
        db.add(new_product)
        await db.commit()
        await db.refresh(new_product)

        return JSONResponse(
            status_code=status.HTTP_201_CREATED,
            content={
                "message": "Product added successfully",
                "product_id": new_product.id
            }
        )

    except HTTPException:
        raise

    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Internal server error"
        )
    
async def update_product(db: AsyncSession, product_id: int, product_data: ProductUpdate) -> JSONResponse:
    try:
        result = await db.execute(select(Product).where(Product.id == product_id))
        existing_product = result.scalar_one_or_none()

        if not existing_product:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Product not found."
            )

        for var, value in vars(product_data).items():
            if value is not None:
                setattr(existing_product, var, value)

        db.add(existing_product)
        await db.commit()
        await db.refresh(existing_product)

        return JSONResponse(
            status_code=status.HTTP_200_OK,
            content={
                "message": "Product updated successfully",
                "product_id": existing_product.id
            }
        )

    except HTTPException:
        raise

    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Internal server error"
        )
    
