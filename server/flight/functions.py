
from .consts import FLIGHTS
from .model import Flight

def generate_schedule():
  schedule = []
  for i in range(len(FLIGHTS)):
    if i == len(FLIGHTS) - 1:
      break
    flight = FLIGHTS[i]
    next_flight = FLIGHTS[i + 1]
    schedule.append(Flight(
      id=i,
      origin=flight["code"],
      destination=next_flight["code"],
      departure=flight["departure"],
      arrival=next_flight["departure"],
      duration=flight["flightTime"],
      waiting_time=flight["waitTime"]
    ))
    
  return schedule