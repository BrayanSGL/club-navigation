
from .consts import DESTINATIONS
from .model import Flight
from datetime import datetime, timedelta

def generate_schedule():
  schedule = []
  initial_date = datetime.now()
  date_departure = initial_date
  
  for i in range(len(DESTINATIONS)):
    if i == len(DESTINATIONS) - 1:
      break
    flight = DESTINATIONS[i]
    next_flight = DESTINATIONS[i + 1]
    
    schedule.append(Flight(
      id=i + 1,
      origin_code=flight["code"],
      origen=flight["name"],
      destination=next_flight["name"],
      destination_code=next_flight["code"],
      departure=date_departure,
      arrival=date_departure + timedelta(minutes=flight["totalTime"]),
      duration=flight["totalTime"],
    ))
    
  return [flight.to_json() for flight in schedule]
