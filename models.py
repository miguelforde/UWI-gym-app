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
  dob = db.Column(db.String(20))
  email = db.Column(db.String(120), unique=True, nullable=False)
  password = db.Column(db.String(120), nullable=False)

  def toDict(self):
    return {
    'fname': self.fname,
    'lname': self.lname,
    'email': self.email,
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
  comment = db.Column(db.String(225))
  creation_date = db.Column(db.DateTime, default = datetime.datetime.now())
  
  def toDict(self):
      return {
          "id": self.id,
          "user_id": self.user_id,
          "comment": self.comment,
          "creation_date": self.creation_date.strftime("%x")
      }

class Workout_Session(db.Model):
  __tablename__ = "Session"
  id = db.Column('id', db.Integer, primary_key = True)
  workout_id = db.Column('workout_id', db.Integer, db.ForeignKey('Workout.id'))
  user_id = db.Column('user_id', db.Integer, db.ForeignKey('User.id'))
  date = db.Column(db.DateTime, default = datetime.datetime.now())
  impression = db.Column(db.CHAR, nullable = False)
  notes = db.Column(db.String(225))
  
  def toDict(self):
      return {
          "id": self.id,
          "workout_id": self.workout_id,
          "user_id": self.user_id,
          "date": self.date.strftime("%x"),
          "impression": self.impression,
          "notes": self.notes
      }
            
class Exercise(db.Model):
  __tablename__ = "Exercise"
  id = db.Column('id', db.Integer, primary_key = True)
  name = db.Column(db.String(225), nullable = False, unique = True)
  description = db.Column(db.String(225), nullable = False,unique = True)
  source = db.Column(db.String(225), nullable = False, unique = True)

  def toDict(self):
      return {
          "id": self.id,
          "name": self.name,
          "description": self.description,
          "source": self.source
      }
    
class Workout_Log(db.Model):
  __tablename__ = "Log"
  id = db.Column('id', db.Integer, primary_key = True)
  exercise_id = db.Column('exercise_id', db.Integer, db.ForeignKey('Exercise.id'))
  user_id = db.Column('user_id', db.Integer, db.ForeignKey('User.id'))
  workout_id = db.Column('workout_id', db.Integer, db.ForeignKey('Workout.id'))
  date = db.Column(db.DateTime, default = datetime.datetime.now(), nullable = False)
  reps = db.Column(db.Integer, nullable = False)
  weight = db.Column(db.Integer, nullable = False)

  def toDict(self):
      return {
          "id": self.id,
          "exercise_id": self.exercise_id,
          "repitition_id": self.repitition_id,
          "user_id": self.user_id,
          "workout_id": self.workout_id,
          "weight_id": self.weight_id,
          "date": self.date.strftime("%x"),
          "reps": self.reps,
          "weight": self.weight
      }
    
class Setting(db.Model):
  __tablename__ = "Setting"
  id = db.Column('id', db.Integer, primary_key = True)
  exercise_id = db.Column('exercise_id', db.Integer, db.ForeignKey('Exercise.id'))
  comment = db.Column(db.String(225))
  reps = db.Column(db.Integer, nullable = False)
  sets = db.Column(db.Integer, nullable = False)
  weight = db.Column(db.Integer, nullable = False)

  def toDict(self):
      return {
          "id": self.id,
          "exercise_id": self.exercise_id,
          "repitition_id": self.repitition_id,
          "weight_id": self.weight_id,
          "comment": self.comment,
          "reps": self.reps,
          "weight": self.weight
      }
