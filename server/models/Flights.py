from .. import db

class Flights(db.Model):
  __tablename__ = 'flights'
  id = db.Column(db.Integer, primary_key=True, autoincrement=True)
  origin = db.Column(db.String(50), nullable=False)
  destination = db.Column(db.String(50), nullable=False)
  duration = db.Column(db.Integer, nullable=False)
  waiting_time = db.Column(db.Integer, nullable=False)
  departure = db.Column(db.String(50), nullable=False)
  arrival = db.Column(db.String(50), nullable=False)

  def __repr__(self):
    return f"<Flights {self.id}>"
    
  