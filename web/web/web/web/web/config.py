import os

class Config:
    SECRET_KEY = os.getenv("SECRET_KEY", "minha_senha_super_secreta")
    SQLALCHEMY_DATABASE_URI = 'sqlite:///site.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
