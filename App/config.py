class Config:
    username ="xxxx"
    password ="xxxx"
    hostname="xxxx"
    port="xxxx"
    database="xxxx"
    SQLALCHEMY_DATABASE_URI=f'mysql+pymysql://{username}:{password}@{hostname}:{port}/{database}'
    SQLALCHEMY_TRACK_MODIFICATIONS=False
    SQLALCHEMY_RECORD_QUERIES=True