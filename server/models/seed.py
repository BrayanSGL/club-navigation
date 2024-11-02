from datetime import datetime, timedelta
from .. import db
from .Flights import Flights
from ..flights import FLIGHTS

def seed_data():
  # Datos por defecto
  default_flights = [
    Flights(
      origin=flight['code'], 
      destination=FLIGHTS[index + 1]['code'] if index + 1 < len(FLIGHTS) else FLIGHTS[0]['code'],
      duration=flight['flightTime'],
      departure=flight['departure'], 
      arrival=(datetime.strptime(flight['departure'], '%H:%M') + timedelta(minutes=flight['flightTime'])).strftime('%H:%M'),
      waiting_time=flight['waiting_time'])
    for index, flight in enumerate(FLIGHTS)
  ]

  # Agregar los productos si no existen
  for flight in default_flights:
    existing_fligth = Flights.query.filter_by(origin=flight.origin, destination=flight.destination).first()
    if not existing_fligth:
      db.session.add(flight)
  
  db.session.commit()
