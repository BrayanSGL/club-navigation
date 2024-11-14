from flask import Flask
from .config import Config
from .database import db
from .routes import register_routes

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    
    # Inicializa la base de datos con la aplicación
    db.init_app(app)

    with app.app_context():
        db.create_all()
        
        # Registra las rutas en la aplicación
        register_routes(app)
        

    return app