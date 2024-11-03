import os
from flask_cors import CORS
from flask import jsonify
from dotenv import load_dotenv  
from .models.User import  User
from . import create_app
from .utils.clock import clock as clock_util

app = create_app()

# Enable CORS globally for the app
CORS(app)


# Cargar las variables de entorno desde el archivo .env
load_dotenv()

# Configuración de la conexión a MySQL utilizando variables de entorno
DB_USER = os.getenv('DB_USER')
DB_PASSWORD = os.getenv('DB_PASSWORD')
DB_HOST = os.getenv('DB_HOST')
DB_NAME = os.getenv('DB_NAME')


# @app.cli.command("init_db")
# def init_db():
#   db.init_app(app)
#   db.create_all()

@app.route('/clock')
def clock():
  return clock_util()
    
# @app.route('/flights/buy', methods=['POST'])
# def buy_flight():
#     data = request.json
#     user_id = data.get('user_id')
#     flight_id = data.get('flight_id')
#     if not user_id or not flight_id:
#         return jsonify({'error': 'Faltan campos obligatorios'}), 400
#     try:
#         user = User.query.get(user_id)
#         if not user:
#             return jsonify({'error': 'Usuario no encontrado'}), 404
#         user.flights.append(flight_id)
#         db.session.commit()
#         return jsonify({'message': 'Vuelo comprado correctamente'}), 201
#     except Exception as e:
#         return jsonify({'error': str(e)}), 500

  
if __name__ == '__main__':
  app.run(host="0.0.0.0" , port=5000) 