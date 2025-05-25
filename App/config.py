import os

class Config:
    username ="admin"
    password ="admin1234"
    hostname="my-portfolio.czmu4so2wyrz.us-east-2.rds.amazonaws.com"
    port="3306"
    database="Equity_Edge"
    SQLALCHEMY_DATABASE_URI = f"mysql+pymysql://{username}:{password}@{hostname}:{port}/{database}"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_RECORD_QUERIES = True

