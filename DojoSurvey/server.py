from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = 'ThisIsSecret'

@app.route('/', methods=['POST'])
def index():
    return render_template("index.html")

@app.route('/result', methods=['POST'])
def create_user():
    print "Recived Post Information"
    session['YourName'] = request.form['YourName']
    session['Location'] = request.form['Location']
    session['Language'] = request.form['Language']
    session['Comment'] = request.form['Comment']
    return redirect('/show')

@app.route('/show')
def result_info():
    return render_template("result.html")

app.run(debug=True)
