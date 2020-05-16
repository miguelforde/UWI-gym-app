import csv
from main import db, Exercises, app 

db.create_all(app=app);

with open('exercises.csv', 'r') as f:
  read = csv.reader(f)

  for row in read:
    exer = { "name": row[0], "target": row[1]}
    exercise = Exercises(name=exer['name'], target=exer['target'])
    db.session.add(exercise)
    db.session.commit()

print ("Database Initialised")
