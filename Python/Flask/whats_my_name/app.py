from flask import Flask, render_template, request, redirect

app = Flask(__name__)

@app.route('/')
def route_home():
    return render_template('index.html')

@app.route('/process', methods=['POST'])
def form_submit():
    print "Name acquired: {}".format(request.form['name'])
    return redirect('/')


app.run(debug=True)