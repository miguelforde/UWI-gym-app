import json
from flask_login import LoginManager, current_user, login_user, login_required, logout_user
from flask import Flask, request, render_template, redirect, flash, url_for, session
from sqlalchemy.exc import IntegrityError
from datetime import timedelta 

from models import db, User, Workout, Setting, Exercises, Exercise
from forms import SignUp, LogIn

''' Begin boilerplate code '''

''' Begin Flask Login Functions '''
login_manager = LoginManager()
@login_manager.user_loader
def load_user(user_id):
  return User.query.get(user_id)

''' End Flask Login Functions '''


def create_app():
  app = Flask(__name__)
  app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
  app.config['SECRET_KEY'] = "MYSECRET"
  app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

  login_manager.init_app(app)
  db.init_app(app)
  return app

app = create_app()

app.app_context().push()
db.create_all(app=app)



@app.route('/signup', methods=['GET', 'POST'])
def signup():
  form = SignUp()
  if form.validate_on_submit():
    data = request.form # get data from form submission
    newuser = User(fname=data['fname'], lname=data['lname'], username=data['username'], dob=data['dob'], email=data['email']) # create user object
    newuser.set_password(data['password']) # set password
    db.session.add(newuser) # save new user
    db.session.commit()
    flash('Account Created!')# send message
    return redirect(url_for('login'))# redirect to login page
  return render_template('signup.html', form=form)


@app.route('/', methods=['GET', 'POST'])
def login():
  form = LogIn()
  if form.validate_on_submit():
    data = request.form
    user = User.query.filter_by(username = data['username']).first() # gets first instance of the user object?
    if user and user.check_password(data['password']): # check credentials
      flash('Logged in successfully.') # send message to next page
      login_user(user) # login the user
      return redirect(url_for('getworkouts'))  # change back to user home
    else:
      flash('Invalid username or password') # send message to next page
      return redirect(url_for('login')) # redirect to login page if login unsuccessful
  return render_template('login.html', form=form, text = "Welcome to The UWI Gym APP")




@app.route('/Workouts', methods = ['GET'])
@login_required
def getworkouts():
    workouts = Workout.query.all()
    return render_template('Workouts.html', workouts=workouts)

@app.route('/Workouts/<id>', methods=['GET'])
@login_required
def getWorkout(id):
  exercise = Exercise.query.filter_by(workout_id = id)
  if setting is None:
    return 'Invalid id or Unauthorized'
  return redirect(urlfor('getWorkout'), workout = setting)

@app.route('/MyWorkouts', methods=['GET'])
@login_required
def getMyWorkouts():
  workout = Workout.query.filter_by(user_id = current_user.id)
  return render_template('MyWorkouts.html',myworkout=workout)

@app.route('/Workouts/<id>', methods=['PUT'])
@login_required
def updateworkout(id):
  workout = Workout.query.get(id)
  if workout == None:
    return 'Invalid id or unauthorized' 
  
  db.session.add(workout)
  db.session.commit()
  return 'Updated', 201 

@app.route('/Workouts/<id>', methods=['Delete'])
@login_required
def deleteworkout():
  workouts = Workout.query.get(id)
  if workout == None:
    return 'Invalid id or unauthorized'
  db.session.delete(workout)
  db.session.commit()
  return 'Deleted', 204

@app.route('/Workouts/<id>', methods=['POST'])
@login_required
def addexercise(id):
  data = request.get_json()
  exercise = Exercise.query.filter_by(name = data['name'])
  exerciseid = exercise.id
  db.session.add(settings)
  db.session.commit() 
  return json.dumps(workout.id)

@app.route('/Workouts/<id1>/Exercises/<id2>', methods=['Delete'])
@login_required
def deleteexercise(id1, id2):
  data = request.get_json()
  workout = Workout.query.get(id1)
  if workout == None:
    return 'Invalid id or unauthorized'
  exercise = Setting.query.filter_by(exercise_id=id2)
  if exercise == None:
    return 'Invalid id or unauthorized'
  db.session.delete(exercies)
  db.session.commit() 
  return 'Deleted', 204


@app.route('/exercises', methods=["GET"])
@login_required
def create_routine():
  exercises = Exercises.query.all()
  return render_template('exercises.html',exercises=exercises)

@app.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect('/')


@app.route("/about")
def about():
  return render_template('about.html')
  
@app.route("/addworkout", methods=["POST", "GET"])
@login_required
def addworkout():
  if request.method == 'POST':
    #user = User.query.filter_by(username = current_user.username)
    workout = Workout(user_id=current_user.id)
    #user = User.query.filter_by(name = session['username']).first()
    #workout = Workout(user_id=user.id)
    count = int(request.form['exercise_count'])
    for i in range(1, count + 1):
      exercise = Exercise(exercise_id = request.form['Exercises' + str(i)], workout_id =workout.id)
      set = Setting(exercise = exercise, reps = request.form['reps' + str(i)], weight = ['weight' + str(i)])
    db.session.add(workout)
    db.session.commit()
    return redirect(url_for('getworkouts'))
  exercises = Exercises.query.all()
  return render_template('addworkout.html', exercises = exercises)


app.run(debug=True, port='4000', host='0.0.0.0')

