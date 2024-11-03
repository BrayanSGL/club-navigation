import os
from flask_cors import CORS
from flask import request, jsonify
from datetime import datetime, timedelta
from dotenv import load_dotenv  
from .models.User import  User
from . import create_app, db
from .utils.clock import clock as clock_util
import jwt

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


@app.cli.command("init_db")
def init_db():
  db.init_app(app)
  db.create_all()

@app.route('/clock')
def clock():
  return clock_util()

# @app.route('/add_user', methods=['POST'])
# def add_user():
#   data = request.json  # Obtener los datos JSON del request

#   # Extraer el nombre de usuario y correo electrónico del JSON
#   username = data.get('username')
#   email = data.get('email')
#   password = data.get('password')

#   # Validar que los campos no estén vacíos
#   if not username or not email or not password:
#     return jsonify({'error': 'Faltan campos obligatorios'}), 400

#   try:
#     # Crear un nuevo usuario con los datos proporcionados
#     new_user = User(username=username, email=email, password=password)

#     # Agregar el nuevo usuario a la sesión de la base de datos
#     db.session.add(new_user)

#     # Confirmar la transacción en la base de datos
#     db.session.commit()

#     return jsonify({'message': 'Usuario agregado correctamente'}), 201

#   except Exception as e:
#     return jsonify({'error': str(e)}), 500

@app.route('/login', methods=['POST'])
def login():
  data = request.json  # Obtener los datos JSON del request

  # Extraer el nombre de usuario y correo electrónico del JSON
  email = data.get('email')
  password = data.get('password')

  # Validar que los campos no estén vacíos
  if  not email or not password:
    return jsonify({'error': 'Faltan campos obligatorios'}), 400

  try:
    # Crear un nuevo usuario con los datos proporcionados
    user = User.query.filter_by(email=email, password=password).first()

    if user:
      token = jwt.encode({'user_id': user.id, 'exp': datetime.utcnow() + timedelta(hours=1)}, "secret", algorithm="HS256")
      return jsonify({'token': token}), 200
    else:
      return jsonify({'error': 'Usuario o contraseña incorrectos'}), 401

  except Exception as e:
    return jsonify({'error': str(e)}), 500
  
@app.route('/users', methods=['GET'])
def get_users():
    users = User.query.all()
    return jsonify([{
        'id': user.id,
        'username': user.username,
        'email': user.email
    } for user in users])
    
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