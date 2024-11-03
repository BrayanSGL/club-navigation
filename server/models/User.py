from ..database import db

class User(db.Model):
  __tablename__ = 'users'
  id = db.Column(db.Integer, primary_key=True, autoincrement=True)
  username = db.Column(db.String(50), nullable=False)
  email = db.Column(db.String(100), nullable=False)
  password = db.Column(db.String(100), nullable=False)
  
  flights = db.relationship('UserFlight', backref='user', lazy=True)

  def __repr__(self):
    return f"<User {self.username}>"