from ..database import db

class UserFlight(db.Model):
  __tablename__ = 'users_flights'
  id = db.Column(db.Integer, primary_key=True, autoincrement=True)
  user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
  flight_id = db.Column(db.Integer, db.ForeignKey('flights.id'), nullable=False)
  
  flight = db.relationship('Flight', back_populates='users')
  user = db.relationship('User', back_populates='flights')

  def __repr__(self):
    return f"<UserFlight {self.id}>"
  
  def to_dict(self):
    return {
      'id': self.id,
      'user_id': self.user_id,
      'flight_id': self.flight_id,
      'flight': self.flight.to_dict()
    }