import os
from flask import Flask, request, jsonify
from datetime import datetime, timedelta
from dotenv import load_dotenv
from .config import Config
from .models.User import  User, db
from . import create_app, db

app = create_app()


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
  now = datetime.now()
  start_of_day = datetime(now.year, now.month, now.day)
  milliseconds_since_start_of_day = (now - start_of_day).total_seconds() * 1000
  new_time = milliseconds_since_start_of_day * 48
  new_date = start_of_day + timedelta(milliseconds=new_time)
  return new_date.strftime('%Y-%m-%d %H:%M:%S')

@app.route('/add_user', methods=['POST'])
def add_user():
  data = request.json  # Obtener los datos JSON del request

  # Extraer el nombre de usuario y correo electrónico del JSON
  username = data.get('username')
  email = data.get('email')
  password = data.get('password')

  # Validar que los campos no estén vacíos
  if not username or not email or not password:
    return jsonify({'error': 'Faltan campos obligatorios'}), 400

  try:
    # Crear un nuevo usuario con los datos proporcionados
    new_user = User(username=username, email=email, password=password)

    # Agregar el nuevo usuario a la sesión de la base de datos
    db.session.add(new_user)

    # Confirmar la transacción en la base de datos
    db.session.commit()

    return jsonify({'message': 'Usuario agregado correctamente'}), 201

  except Exception as e:
    return jsonify({'error': str(e)}), 500
    
  
if __name__ == '__main__':
  app.run(host="0.0.0.0" , port=5000) 