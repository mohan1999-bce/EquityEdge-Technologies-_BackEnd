from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker,declarative_base
from App.config import get_cnx_string

connection_string=get_cnx_string()

engine = create_engine(connection_string)
SessionLocal = sessionmaker(bind=engine)
Base = declarative_base()

def get_session():
    return SessionLocal()