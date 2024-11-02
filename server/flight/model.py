class Flight():
  def __init__(self, id, origin, destination, departure, arrival, duration, waiting_time):
    self.id = id
    self.origin = origin
    self.destination = destination
    self.departure = departure
    self.arrival = arrival
    self.duration = duration
    self.waiting_time = waiting_time

  def __repr__(self):
    return f"<Fligth {self.id}>"

  def to_json(self):
    return {
      "id": self.id,
      "origin": self.origin,
      "destination": self.destination,
      "departure": self.departure,
      "arrival": self.arrival,
      "duration": self.duration,
      "waiting_time": self.waiting_time
    }