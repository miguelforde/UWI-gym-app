import sqlalchemy
from werkzeug.security import generate_password_hash, check_password_hash
import datetime

db = sqlalchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)

    def toDict(self):
      return {
        "id": self.id,
        "username": self.username,
        "email": self.email,
        "password":self.password
      }
    
    def set_password(self, password):
        """Create hashed password."""
        self.password = generate_password_hash(password, method='sha256')

    def check_password(self, password):
        """Check hashed password."""
        return check_password_hash(self.password, password)

class Workout(db.Model):
    id = db.Column('id', db.Integer, primary_key = True)
    user_id = db.Column('user_id', db.Integer, db.Foriegnkey('User.id'))
    comment = db.Column(db.String(225))
    creation_date = db.Column(db.dateTime.datetime.date())
    
    def toDict(self):
        return {
            "id": self.id,
            "user_id": self.user_id,
            "comment": self.comment,
            "creation_date": self.creation_date.strftime("%x")
        }

class Workout_Session(db.Model):
    id = db.Column('id', db.Integer, primary_key = True)
    workout_id = db.Column('workout_id', db.Integer, db.Foreignkey('Workout.id'))
    user_id = db.Column('user_id', db.Integer, db.Foreignkey('User.id'))
    date = db.Column(db.dateTime.datetime.date())
    impression = db.Column(db.CHAR, nullable = False)
    notes = db.Column(db.String(225))
    
    def toDict(self):
        return {
            "id": self.id,
            "workout_id": self.workout_id,
            "user_id": self.user_id,
            "date": self.date.strftime("%x")
        }
            
class Weight(db.Model):
    id = db.Column('id', db.Integer, primary_key = True)
    value = db.Column(db.Integer, nullable = False)

    def toDict(self):
        return {
            "id": self.id,
            "value": self.value
        }

class Exercise(db.Model):
    id = db.Column('id', db.Integer, primary_key = True)
    name = db.Column(db.String(225), nullable = False, unique = True)

    def toDict(self):
        return {
            "id": self.id,
            "name": self.name
        }
    
class Repitition(db.Model):
    id = db.Column('id', db.Integer, primary_key = True)
    value = db.Column(db.Integer, nullable = False)

    def toDict(self):
        return {
            "id": self.id,
            "value": self.value
        }
    
class Workout_Log(db.Model):
    id = db.Column('id', db.Integer, primary_key = True)
    exercise_id = db.Column('exercise_id', db.Integer, db.ForeignKey('Exercise.id'))
    repitition_id = db.Column('repitition_id', db.Integer, db.Foreignkey('Repitition.id'))
    user_id = db.Column('user_id', db.Integer, db.ForeignKey('User.id'))
    workout_id = db.Column('workout_id', db.Integer, db.Foreignkey('Workout.id'))
    weight_id = db.Column('weight_id', db.Integer, db.ForeignKey('Weight.id'))
    date = db.Column(db.dateTime.dateTime.now(), nullable = False)
    reps = db.Column(db.Integer, db.select([Repitition.value]).where(Repitition.id == repitition_id))
    weight = db.Column(db.Decimal, db.select([Weight.value]).where(Weight.id == weight_id))

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
    id = db.Column('id', db.Integer, primary_key = True)
    exercise_id = db.Column('exercise_id', db.Integer, db.ForeignKey('Exercise.id'))
    repitition_id = db.Column('repitition_id', db.Integer, db.Foreignkey('Repitition.id'))
    weight_id = db.Column('weight_id', db.Integer, db.ForeignKey('Weight.id'))
    comment = db.Column(db.String(225))
    reps = db.Column(db.Integer, db.select([Repitition.value]).where(Repitition.id == repitition_id))
    weight = db.Column(db.Decimal, db.select([Weight.value]).where(Weight.id == weight_id))

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
