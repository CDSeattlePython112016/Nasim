from flask import Flask, render_template, session, redirect, request
app = Flask(__name__)
import random
app.secret_key = 'ThisIsSecret'

@app.route('/')
def index():
    if 'number' not in session:
        session['number'] = random.randint(1, 100)
    return render_template('index.html')

@app.route('/guess',  methods =["POST"])
def guess():
    current = int(request.form['result'])
    if current < session['number']:
        session['result']='low'
    elif current > session['number']:
        session['result'] = 'high'
    elif current == session['number']:
        session['result'] = 'correct'

    return redirect('/')

@app.route('/reset', methods = ['POST'])
def reser():
    session.clear()
    return redirect('/')











app.run(debug=True)

    # if guess > session['number']:
    #     print('Too high.')
    # elif guess < session['number']:
    #     print('Too low')
    # elif guess == session['number']:
    #     print('number was the number!')
