from flask import Blueprint, jsonify, request
from ..models.UserFlight import UserFlight
from ..flight.functions import generate_schedule

flights_bp = Blueprint('flights', __name__, url_prefix='/flights')

@flights_bp.route('/', methods=['GET'])
def get_flights():
  flights = generate_schedule()
  return jsonify(flights)

@flights_bp.route('/<int:id>/register', methods=['POST'])
def register_flight(id):
  data = request.json
  user_id = data.get('user_id')
  
  user_flight = UserFlight(user_id=user_id, flight_id=id)
  user_flight.save()
  return jsonify({'message': 'Vuelo registrado correctamente'}), 201