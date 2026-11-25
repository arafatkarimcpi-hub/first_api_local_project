from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

#DATABASE_URL = "mysql+pymysql://root:root@localhost:3306/training"
DATABASE_URL="postgresql+psycopg2://training_zpqp_user:JX8NuaVCOxowcXN4Vx7Vv4bdKOCyfh1H@dpg-dc35cr9ksfps7392o5f0-a.oregon-postgres.render.com/training_zpqpn-postgres.render.com/training_l3ic"
engine = create_engine(DATABASE_URL)
session_local = sessionmaker(autocommit = False, autoflush= False, bind=engine)
base = declarative_base()


# def get_connection():
#     db = session_local()
#     try:
#         yield db
#     finally:
#         db.close