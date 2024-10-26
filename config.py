import os

BASE_DIR = os.path.abspath(os.path.dirname(__file__))

class Config:
    SQLALCHEMY_DATABASE_URI = f'sqlite:///{os.path.join(BASE_DIR, "users_info.db")}'
    SQLALCHEMY_TRACK_MODIFACATION = False
    SECRET_KEY = os.getenv("SECRET_KEY", "default_key")