from .. import db

class UserFlight(db.Model):
  __tablename__ = 'users_flights'
  id = db.Column(db.Integer, primary_key=True, autoincrement=True)
  user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
  flight_id = db.Column(db.Integer, nullable=False)

  def __repr__(self):
      return f"<UserFlight {self.id}>"