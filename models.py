from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
import datetime 

db = SQLAlchemy()

class User(db.Model, UserMixin):
  __tablename__ = "User"
  id = db.Column(db.Integer, primary_key=True)
  fname = db.Column(db.String(50), nullable=False)
  lname = db.Column(db.String(50), nullable=False)
  username = db.Column(db.String(50), nullable=False, unique=True)
  dob = db.Column(db.String(20))
  email = db.Column(db.String(120), unique=True, nullable=False)
  password = db.Column(db.String(120), nullable=False)
  workouts = db.relationship('Workout', backref = 'user', lazy = 'dynamic')

  def toDict(self):
    return {
    'fname': self.fname,
    'lname': self.lname,
    'email': self.email,
    'username': self.username,
    'dob': self.dob
    }

  def set_password(self, password):
    self.password = generate_password_hash(password, method='sha256')

  def check_password(self, password):
    return check_password_hash(self.password,password)

class Workout(db.Model):
  __tablename__ = "Workout"
  id = db.Column('id', db.Integer, primary_key = True)
  user_id = db.Column('user_id', db.Integer, db.ForeignKey('User.id'))
  name = db.Column(db.String(225))
  exercises = db.relationship('Exercise', backref = 'workout', lazy = 'dynamic')
  
  def toDict(self):
      return {
          "id": self.id,
          "user_id": self.user_id,
          "name": self.name
      }
    
# using csv file
class Exercises(db.Model):
  id = db.Column(db.Integer, primary_key = True)
  name = db.Column(db.String(120))
  target = db.Column(db.String(120))

  def toDict(self):
    return {
      "name" : self.name,
      "target" : self.target
    }

class Exercise(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  workout_id = db.Column(db.Integer, db.ForeignKey('Workout.id'))
  exercise_id = db.Column(db.Integer, db.ForeignKey('exercises.id'))
  sets = db.relationship('Setting', backref ='exercise', lazy = 'dynamic') #db.Column(db.String(10))
  reps = db.Column(db.String(10))

class Setting(db.Model):
  __tablename__ = "Setting"
  id = db.Column('id', db.Integer, primary_key = True)
  exercise_id = db.Column('exercise_id',db.Integer, db.ForeignKey(Exercise.id))
  reps = db.Column(db.Integer, nullable = False)
  weight = db.Column(db.Integer, nullable = False)

  def toDict(self):
      return {
          "id": self.id,
          "reps": self.reps,
          "weight": self.weight
      }
