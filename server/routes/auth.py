from flask import Blueprint, jsonify, request
import jwt
from datetime import datetime, timedelta
from ..models.User import User

auth_bp = Blueprint('auth', __name__, url_prefix='/auth')

@auth_bp.route('/login', methods=['POST'])
def login():
  data = request.json
  email = data.get('email')
  password = data.get('password')
  
  if not email or not password:
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
  
