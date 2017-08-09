from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def print_index():
    return render_template('index.html')

@app.route('/about')
def print_about():
    return render_template('about.html')

@app.route('/projects')
def print_projects():
    return render_template('portfolio.html')

app.run(debug=True)