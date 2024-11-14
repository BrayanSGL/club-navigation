class Flight():
  def __init__(self, id, origin_code, origen, destination, destination_code, departure, arrival, duration):
    self.id = id
    self.origin_code = origin_code
    self.origin = origen
    self.destination = destination
    self.destination_code = destination_code
    self.departure = departure
    self.arrival = arrival
    self.duration = duration

  def __repr__(self):
    return f"<Fligth {self.id}>"

  def to_json(self):
    return {
      "id": self.id,
      "origin_code": self.origin_code,
      "origin": self.origin,
      "destination": self.destination,
      "destination_code": self.destination_code,
      "departure": self.departure,
      "arrival": self.arrival,
      "duration": self.duration,
    }