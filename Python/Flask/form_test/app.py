from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)
app.secret_key = 'goop6482WEstopFUN993pin'

@app.route('/')
def route_home():
    return render_template('index.html')

@app.route('/users', methods=['POST'])
def create_user():
    print "Got post info"
    session['name'] = request.form['name']
    session['email'] = request.form['email']
    return redirect('/show')

@app.route('/show')
def show_user():
  return render_template('user.html')

app.run(debug=True)