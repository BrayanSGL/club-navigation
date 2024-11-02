from .flights import flights_bp

def register_routes(app):
  app.register_blueprint(flights_bp)