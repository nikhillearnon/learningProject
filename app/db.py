# # app/db.py
# import os
# from sqlmodel import create_engine, SQLModel, Session
# from dotenv import load_dotenv

# # load .env from project root (optional)
# load_dotenv()

# DB_USER = os.getenv("DB_USER", "root")
# DB_PASSWORD = os.getenv("DB_PASSWORD", "")
# DB_HOST = os.getenv("DB_HOST", "127.0.0.1")
# DB_PORT = os.getenv("DB_PORT", "3306")
# DB_NAME = os.getenv("DB_NAME", "fastapi_auth")

# # SQLAlchemy url for pymysql driver
# DATABASE_URL = f"mysql+pymysql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

# # echo=True will print SQL to console (helpful for debugging)
# engine = create_engine(DATABASE_URL, echo=False)

# def create_db_and_tables():
#     # Will create tables for all SQLModel models in metadata
#     SQLModel.metadata.create_all(engine)

# def get_session():
#     with Session(engine) as session:
#         yield session
