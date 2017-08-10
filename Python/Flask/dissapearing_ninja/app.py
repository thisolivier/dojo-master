from flask import Flask, render_template, request, redirect

app = Flask(__name__)

@app.route('/')
def route_home():
    return render_template('index.html')

@app.route('/ninja')
def homeboys():
    print "Got post info"
    return render_template('ninjas.html')

@app.route('/ninja/<color>')
def homeboy(color):
    print "{} Ninja requested".format(color)
    return render_template('ninja.html', color=color)


app.run(debug=True)