from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def route_root():
    return render_template('root.html')

@app.route('/results', methods=['POST'])
def parse_form():
    na = request.form['name']
    loc = request.form['location']
    lang = request.form['language']
    com = request.form['comment']
    return render_template('results.html', name=na, location=loc, language=lang, comment=com )

app.run(debug=True)