from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

#DATABASE_URL = "mysql+pymysql://root:root@localhost:3306/training"
#DATABASE_URL="postgresql+psycopg2://training_zpqp_user:JX8NuaVCOxowcXN4Vx7Vv4bdKOCyfh1H@dpg-dc35cr9ksfps7392o5f0-a.oregon-postgres.render.com/training_zpqpn-postgres.render.com/training_l3ic"
#DATABASE_URL="postgresql+psycopg2:kTy0gwfhQdfKDhXd8FQp8MHOxaLHLuX7@dpg-dc36kd2jnfac73b5609g-a.oregon-postgres.render.com/training_zbvy"
DATABASE_URL="postgresql+psycopg2://training_qq0j_user:k0ooA2hyF8RWsCFKhkC8aU1jerKSD9aS@dpg-dc3a23e7bikc73cje0r0-a.oregon-postgres.render.com/training_qq0j"
engine = create_engine(DATABASE_URL)
session_local = sessionmaker(autocommit = False, autoflush= False, bind=engine)
base = declarative_base()

# def get_connection():
#     db = session_local()
#     try:
#         yield db
#     finally:
#         db.close
