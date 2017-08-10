from flask import Flask, render_template, request, redirect

app = Flask(__name__)

@app.route('/')
def route_home():
    return render_template('index.html')

@app.route('/users', methods=['POST'])
def create_user():
    print "Got post info"
    name = request.form['name']
    email = request.form['email']
    return redirect('/')


app.run(debug=True)