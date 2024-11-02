from flask import Blueprint, jsonify
from ..flight.consts import generate_schedule

flights_bp = Blueprint('flights', __name__, url_prefix='/flights')

@flights_bp.route('/', methods=['GET'])
def get_flights():
  flights = generate_schedule()
  return jsonify(flights)

# @flights_bp.route('/<int:id>/register', methods=['POST'])