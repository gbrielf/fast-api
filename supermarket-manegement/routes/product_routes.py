# layer responsible for expose the API, receiving client requisitions and returning responses 
from typing import List
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from core.database import SessionLocal
from schemas.product import ProductCreate, ProductUpdate, ProductResponse
from services.product_service import create_product, update_product
from repositories.product_repository import list as list_products_db, search_by_id, delete as delete_product_db

router = APIRouter(prefix="/product", tags=["Products"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/", response_model=ProductResponse)
def create(data: ProductCreate, db: Session = Depends(get_db)):
    return create_product(db, data)


@router.get("/", response_model=List[ProductResponse])
def list_products(db: Session = Depends(get_db)):
    return list_products_db(db)


@router.get("/{product_id}", response_model=ProductResponse)
def search(product_id:int, db: Session = Depends(get_db)):
    product = search_by_id(db, product_id)

    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    
    return product


@router.put("/{product_id}", response_model=ProductResponse)
def update(product_id: int, data: ProductUpdate, db: Session = Depends(get_db)):
    product = search_by_id(db, product_id)

    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    
    return update_product(db, product, data)


@router.delete("/{product_id}")
def delete(product_id:int, db:Session = Depends(get_db)):
    product = search_by_id(db, product_id)

    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
                            
    delete_product_db(db, product)
    return {"mensagem": "Product deleted with sucess"}