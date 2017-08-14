from flask import Flask, render_template, session, request, redirect
from random import randint
from time import strftime, gmtime

app = Flask(__name__)
app.secret_key = "bfr7w942p3ubfrug79s4uyoe90sz1"

@app.route('/')
def main_page():
    try:
        session['gold_count']
    except:
        session['gold_count'] = 0
        session['logs'] = []
    return render_template('index.html')

@app.route('/golds', methods=['post'])
def calculate_gold():
    mini_db = {
        'hospital' : (10, 50),
        'church' : (-5, 10),
        'gardening' : (2, 7),
        'strippers' : (-100, -50),
        'vortex' : (-200, 200),
    }
    location = request.form['location']
    l_range = mini_db[location]
    gold_found = randint(l_range[0], l_range[1])
    time = strftime('%Y-%m-%d %H:%I:%S', gmtime())
    log = {
        'location' : location,
        'gold' : gold_found,
        'time' : time,
    }
    session['gold_count'] += gold_found
    session['logs'].insert(0, log)
    return redirect('/')

@app.route('/reset', methods=['post'])
def reset():
    del session['gold_count']
    del session['logs']
    return redirect('/')

app.run(debug=True)