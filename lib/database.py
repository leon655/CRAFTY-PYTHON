from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

Base = declarative_base()
engine = create_engine("sqlite:///blue_collar.db")
Session = sessionmaker(bind=engine)
session = Session()

def initialize_database():
    Base.metadata.create_all(engine)
