class Fligth():
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
