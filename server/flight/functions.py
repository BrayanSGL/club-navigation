
from .consts import DESTINATIONS
from .model import Flight
from datetime import datetime, timedelta
from ..utils.clock import clock

def generate_schedule():
  schedule = []
  time_now = clock()
  print(time_now, "time")
  initial_date = datetime.strptime(time_now, "%Y-%m-%d %H:%M:%S")
  date_departure = initial_date
  
  for i in range(len(DESTINATIONS)):
    next_flight = None
    if i == len(DESTINATIONS) - 1:
      next_flight = DESTINATIONS[0]
    else:
      next_flight = DESTINATIONS[i + 1]
      
    flight = DESTINATIONS[i]
    
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
    
    date_departure = date_departure + timedelta(minutes=flight["totalTime"])
    
  return [flight.to_json() for flight in schedule]
