from flask import Flask, render_template, request, redirect, session, flash
app = Flask(__name__)
app.secret_key = "It's a secret!"

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/ninjas')
def turtles():
    mutant = True
    return render_template("ninja.html", mutant=mutant)

@app.route('/ninjas/<color>')
def ninja(color):
    mutant = False
    return render_template("ninja.html", color=color, mutant=mutant)

app.run(debug=True)
