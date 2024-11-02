from flask import Blueprint, jsonify
from ..models.Flights import Flights

flights_bp = Blueprint('flights', __name__, url_prefix='/flights')

@flights_bp.route('/', methods=['GET'])
def get_flights():
  flights = Flights.query.all()
  return jsonify(flights)