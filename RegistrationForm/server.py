
from flask import Flask, render_template, redirect, request, session, flash
import re

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
NAME_REGEX = re.compile(r'^[a-zA-Z]+$')
PASSWORD_REGEX = re.compile(r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d).+$')

app = Flask(__name__)
app.secret_key = "ThisIsSecret!"

@app.route('/', methods=['GET'])
def index():
  return render_template("index.html")

@app.route('/registration', methods=['POST'])
def submit():
    if len(request.form['first_name']) == 0:
        flash("First name cannot be blank!")

    elif not NAME_REGEX.match(request.form['first_name']):
        flash("Name cannot contain numbers")
    elif len(request.form['last_name']) == 0:
        flash("Last name cannot be blank!")
    elif not NAME_REGEX.match(request.form['last_name']):
        flash("Name cannot contain numbers")

    elif len(request.form['email']) == 0:
        flash("Email cannot be blank!")
    elif not EMAIL_REGEX.match(request.form['email']):
        flash("Invalid Email Address!")

    elif len(request.form['birthday']) == 0:
        flash("Birthday field may not be blank!")

    elif len(request.form['password']) < 8:
        flash("Password must be at least 8 charicters.")
    elif not PASSWORD_REGEX.match(request.form['password']):
        flash("Password must contain at least one capital letter and one number.")
    elif not request.form['confirm'] == request.form['password']:
        flash("Password does not match.")
    else:
        flash("Thanks for submitting your information")

    return redirect('/')

app.run(debug=True)
