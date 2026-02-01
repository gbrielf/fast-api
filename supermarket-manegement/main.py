# main point of entry ino the application
from fastapi import FastAPI
from core.database import engine, Base
from routes.product_routes import router as product_router
from sqlalchemy import create_engine
# establishing a source of connectivity to a specific database
from sqlalchemy.orm import sessionmaker, declarative_base
# session maker is a factory function used to create new Session objects with a consistent configuration
# and declarative base is a foundational class that allows you to define object-relational mapping (ORM) models

DATABASE_URL = "sqlite:///./supermercado.db"

# if the tables in the DB doesn't exists it will be created, this action are made for facilitate the execution of script dependences on extern SQL   
Base.metadata.create_all(bind=engine)

app = FastAPI(title="API for manager supermarkets")

app.include_router(product_router)

# Conection creation with the DB started
# the "engine" is responsable for send and receive comands SQL
engine = create_engine(
    DATABASE_URL, connect_args={"check_same_thread": False}
)
# check_same_thread = False prevents a connection from being user by more than one thread, because limitations of SQLite with multiple threads

SessionLocal = sessionmaker(
    autocommit=False, # commit = False: forces execution of commit for generate data persistence
    autoflush=False, # preventes automatic changes of data on DB
    bind=engine # engine is the central point of SQL commands send and received 
)

Base = declarative_base()
# define the base ORM class that allow transform Python classes on DB tables
