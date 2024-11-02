from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from .config import Config

# Inicializa SQLAlchemy
db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    
    # Inicializa la base de datos con la aplicación
    db.init_app(app)

    with app.app_context():
        # Crea las tablas en la base de datos si no existen
        db.create_all()
        
        # Registra las rutas en la aplicación
        from .routes import register_routes
        register_routes(app)
        

    return app