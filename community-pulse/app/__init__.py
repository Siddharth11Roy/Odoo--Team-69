from flask import Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager
from flask_mail import Mail
from .routes.home import home_bp
from dotenv import load_dotenv
import os


db=SQLAlchemy()
jwt=JWTManager()
mail=Mail()
cors = CORS()

def create_app():
    load_dotenv() #load .env variables
    
    app=Flask(__name__)
    app.config.from_object("app.config.Config")
    
    app.register_blueprint(home_bp)
    db.init_app(app)
    jwt.init_app(app)
    mail.init_app(app)
    cors.init_app(app)

   
    
    return app

