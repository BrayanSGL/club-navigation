
from .consts import DESTINATIONS
from .model import Flight

def generate_schedule():
  schedule = []
  for i in range(len(DESTINATIONS)):
    if i == len(DESTINATIONS) - 1:
      break
    flight = DESTINATIONS[i]
    next_flight = DESTINATIONS[i + 1]
    schedule.append(Flight(
      id=i + 1,
      origin=flight["code"],
      destination=next_flight["code"],
      departure=flight["departure"],
      arrival=next_flight["departure"],
      duration=flight["flightTime"],
    ))
    
  return [flight.to_json() for flight in schedule]
