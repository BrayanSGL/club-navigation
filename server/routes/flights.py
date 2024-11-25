from flask import Blueprint, jsonify, request
from ..models.UserFlight import UserFlight
from ..database import db
from ..flight.functions import generate_schedule
from ..models.Flights import Flight
from ..utils.clock import clock

flights_bp = Blueprint('flights', __name__, url_prefix='/flights')

@flights_bp.route('/', methods=['GET'])
def get_flights():
  # traer los vuelos que estan en el futuro desde hoy
  today = clock()
  flights_server = Flight.query.filter(Flight.departure >= today).all()
  
  if len(flights_server) == 0:
    flights = generate_schedule()
    for flight in flights:
      db.session.add(flight)
  elif len(flights_server) < 6:
    last_flight = flights_server[-1]
    flights = generate_schedule(last_flight.departure)
    for flight in flights:
      db.session.add(flight)
  else:
    return jsonify([flight.to_json() for flight in flights_server])
 
  flights_server = Flight.query.filter(Flight.departure >= today).all()
  
  return jsonify([flight.to_json() for flight in flights_server])

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