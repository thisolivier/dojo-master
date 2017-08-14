from flask import Flask, render_template, session, request
from random import randint

app = Flask(__name__)
app.secret_key = "754807043bguo74bf734bm237"

@app.route('/')
def root_display():
    session['my_num'] = randint(1,100)
    return render_template('index.html')
    
@app.route('/evaluate', methods=['post'])
def do_results():
    session['human_num'] = int(request.form['guess'])
    return render_template('results.html')

app.run(debug=True)