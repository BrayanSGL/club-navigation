from flask import Blueprint, jsonify, request
from ..models.User import User

users_bp = Blueprint('users', __name__, url_prefix='/users')

@users_bp.route('/', methods=['GET'])
def get_users():
  users = User.query.all()
  return jsonify([{
    'id': user.id,
    'username': user.username,
    'email': user.email,
    'flights': [flight.to_dict() for flight in user.flights]
  } for user in users])