import random
from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = 'ThisIsSecret'


@app.route('/')
def index():
    if 'yourGold' not in session:
        session['yourGold'] = 0

    if 'activity_log' not in session:
        session['activity_log'] = []

    return render_template('index.html')

@app.route('/process_money', methods=['POST'])
def process_money():
    building = request.form['building']

    if building == 'farm':
        newGold = random.randint(10, 20)
        session['yourGold'] += newGold
    elif building == 'cave':
        newGold = random.randint(5, 10)
        session['yourGold'] += newGold
    elif building == 'house':
        newGold = random.randint(2, 5)
        session['yourGold'] += newGold
    elif building == 'casino':
        newGold = random.randint(-50, 50)
        session['yourGold'] += newGold

    new_activity = {
        "activity":"you {} {} from the {}".format("earned" if newGold > 0 else "lost", abs(newGold), building),
        "color": "green" if newGold > 0 else "red",
    }

    session['activity_log'].append(new_activity)

    return redirect('/')

@app.route('/reset')
def reset():
    session.clear()
    return redirect('/')

app.run(debug=True)
