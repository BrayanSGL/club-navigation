from flask import Blueprint, jsonify, request
from datetime import datetime
from ..models.UserFlight import UserFlight
from ..database import db
from ..flight.functions import generate_schedule
from ..models.Flights import Flight

flights_bp = Blueprint('flights', __name__, url_prefix='/flights')

@flights_bp.route('/', methods=['GET'])
def get_flights():
  # traer los vuelos que estan en el futuro desde hoy
  # today = datetime.now().date()
  # flights = Flight.query.filter(Flight.date >= today).all()
  
  flights = generate_schedule()
  return jsonify(flights)

@flights_bp.route('/<int:id>/register', methods=['POST'])
def register_flight(id):
  data = request.json
  user_id = data.get('user_id')
  
  if not user_id:
    return jsonify({'error': 'Faltan campos obligatorios'}), 400
  
  user_flight = UserFlight(user_id=user_id, flight_id=id)
  db.session.add(user_flight)
  db.session.commit()
  return jsonify({'message': 'Vuelo registrado correctamente'}), 201