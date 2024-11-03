from .flights import flights_bp
from .users import users_bp

def register_routes(app):
  app.register_blueprint(flights_bp)
  app.register_blueprint(users_bp)