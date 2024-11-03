from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from .config import Config
from .database import db
from .routes import register_routes

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    
    # Inicializa la base de datos con la aplicación
    db.init_app(app)

    with app.app_context():
        # Crea las tablas en la base de datos si no existen
        # from .models.UserFlight import UserFlight
        # from .models.User import User
        
        db.create_all()
        print('Base de datos inicializada')
        
        # Registra las rutas en la aplicación
        register_routes(app)
        

    return app