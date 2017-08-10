from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)
app.secret_key = "boo"

@app.route('/')
def route_home():
    if 'counter' not in session.keys():
        session['counter'] = 0
    return render_template('index.html')

@app.route('/users', methods=['POST'])
def create_user():
    if request.form['howMany'] == "reset" :
        session['counter'] = 0
    else :
        session['counter'] += int(request.form['howMany'])
    print "Counter at", session['counter']
    return redirect('/')


app.run(debug=True)