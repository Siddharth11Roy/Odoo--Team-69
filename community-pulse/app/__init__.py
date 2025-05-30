from flask import Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager
from flask_mail import Mail


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

    db.init_app(app)
    jwt.init_app(app)
    mail.init_app(app)
    cors.init_app(app)
    
   
        
    # app.register_blueprint(home_bp)
    # app.register_blueprint(auth, url_prefix='/auth')
    from .routes import register_blueprints
    register_blueprints(app)

   
    
    return app

