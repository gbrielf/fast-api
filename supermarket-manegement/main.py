# main point of entry into the application
from fastapi import FastAPI
from routes.product_routes import router as product_router
from core.database import engine, Base

# if the tables in the DB doesn't exists it will be created
Base.metadata.create_all(bind=engine)

app = FastAPI(title="API for management of supermarkets")

app.include_router(product_router)
