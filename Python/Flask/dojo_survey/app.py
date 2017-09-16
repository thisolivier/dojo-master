from flask import Flask, render_template, request, redirect, flash

app = Flask(__name__)

app.secret_key = 'b@r)qIkVt-e`wQQhkS=jn{4t0MyEv*nqta|2/dtQG<?[r%|QhI8^CZcOOXXql95}'

@app.route('/')
def route_root():
    return render_template('root.html')

@app.route('/results', methods=['POST'])
def parse_form():
    na = request.form['name']
    loc = request.form['location']
    lang = request.form['language']
    com = request.form['comment']
    for field in [na,com]:
        if len(field) == 0:
            flash("Please fill in all the fields!")
            return redirect('/')
    if len(com) > 120:
        flash("Your comment was too long, please keep it brief.")
        return redirect('/')
    return render_template('results.html', name=na, location=loc, language=lang, comment=com )

app.run(debug=True)