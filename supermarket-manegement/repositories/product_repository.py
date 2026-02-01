# responsible for persistence operations in DB
from sqlalchemy.orm import Session
from models.product import Product

def create(db: Session, product: Product):
    db.add(product)
    db.commit() # commit is the primary action for persisting data
    db.refresh(product) # and refresh ensures that the returned object is synchronized with the DB state
    return product

# returns all register products
def list(db: Session):
    return db.query(Product).all()

# allows regain one specific object
def search_by_id(db: Session, product_id: int):
    return db.query(Product).filter(Product.id == product_id).first()

# allow update data of one specific object
def update(db: Session, product: Product, updated_data: dict):
    for field, value in updated_data.items():
        setattr(product, field, value)
    
    # after changing update fields in a specific object the commit is necessary to persist the data.
    db.commit()
    db.refresh(product)
    return product

def delete(db: Session, product: Product):
    db.delete(product)
    db.commit()