from .. import db
from .Flights import Flights
from ..flights import FLIGHTS

def seed_data():
  # Datos por defecto
  default_flights = [
    Flights(
      origin=flight['code'], 
      destination=FLIGHTS[index + 1]['code'], 
      duration=flight['duration'], 
      departure=flight['departure'], 
      arrival=flight['arrival'], 
      waiting_time=flight['waiting_time'])
    for flight, index in FLIGHTS
  ]

  # Agregar los productos si no existen
  for flight in default_flights:
    existing_fligth = Flights.query.filter_by(origin=flight.origin, destination=flight.destination).first()
    if not existing_fligth:
      db.session.add(flight)
  
  db.session.commit()
