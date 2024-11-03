from ..database import db

class Flight(db.Model):
  __tablename__ = 'flights'
  id = db.Column(db.Integer, primary_key=True)
  origin = db.Column(db.String(3), nullable=False)
  destination = db.Column(db.String(3), nullable=False)
  departure = db.Column(db.String(5), nullable=False)
  arrival = db.Column(db.String(5), nullable=False)
  duration = db.Column(db.String(5), nullable=False)
  waiting_time = db.Column(db.String(5), nullable=False)
  
  def __repr__(self):
    return f"<Flight {self.origin} to {self.destination}>"
  