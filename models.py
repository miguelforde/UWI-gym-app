import sqlalchemy
import datetime

db = sqlalchemy()

class Workout(db.model):
    id = db.Column('id', db.Integer, primary_key = True)
    user_id = db.Column('user_id', db.Integer, db.Foriegnkey('User.id'))
    comment = db.Column(db.String(225))
    creation_date = db.Column(db.DateTime.date())


class Workout_Session(db.model):
    id = db.Column('id', db.Integer, primary_key = True)
    workout_id = db.Column('workout_id', db.Integer, db.Foreignkey('Workout.id'))
    user_id = db.Column('user_id', db.Integer, db.Foreignkey('User.id'))
    date = db.Column(db.DateTime.date())
    impression = db.Column(db.CHAR, nullable = False)
    notes = db.Column(db.String(225))

class Weight(db.model):
    id = db.Column('id', db.Integer, primary_key = True)
    value = db.Column(db.Integer, nullable = False)

class Exercise(db.model):
    id = db.Column('id', db.Integer, primary_key = True)
    name = db.Column(db.String(225), nullable = False, unique = True)

class Repitition(db.model):
    id = db.Column('id', db.Integer, primary_key = True)
    value = db.Column(db.Integer, nullable = False)

class Workout_Log(db.model):
    id = db.Column('id', db.Integer, primary_key = True)
    exercise_id = db.Column('exercise_id', db.Integer, db.ForeignKey('Exercise.id'))
    repitition_id = db.Column('repitition_id', db.Integer, db.Foreignkey('Repitition.id'))
    user_id = db.Column('user_id', db.Integer, db.ForeignKey('User.id'))
    workout_id = db.Column('workout_id', db.Integer, db.Foreignkey('Workout.id'))
    weight_id = db.Column('weight_id', db.Integer, db.ForeignKey('Weight.id'))
    date = db.Column(db.DateTime.Today(), nullable = False)
    reps = db.Column(db.Integer, db.select([Repitition.value]).where(Repitition.id == repitition_id))
    weight = db.Column(db.Decimal, db.select([Weight.value]).where(Weight.id == weight_id))





