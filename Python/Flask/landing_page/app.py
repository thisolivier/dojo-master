from flask import Flask, render_template, request, redirect

app = Flask(__name__)

@app.route('/')
def route_home():
    return render_template('index.html')

@app.route('/ninjas')
def route_ninjas():
    return render_template('ninjas.html')

@app.route('/dojos/new')
def create_dojo():
    return render_template('dojos.html')


app.run(debug=True)