from flask import Flask, render_template, redirect, flash, request
import re
import datetime

app = Flask(__name__)
app.secret_key = 'UEpcbOV+G6Z+>}st)EOJSp?>Zm+h+wi?t4id-XMyqj8ZuO|;C${G+Dz{S^$80Yp='

@app.route('/')
def root_route():
    print "Route root function called"
    return render_template('/portal.html')

@app.route('/process', methods=['POST'])
def process_form():
    em = request.form['email']
    na_1 = request.form['first_name']
    na_2 = request.form['last_name']
    pwd_1 = request.form['password']
    pwd_2 = request.form['password_c']
    try:
        b_d = int(request.form['day'])
        b_m = int(request.form['month'])
        b_y = int(request.form['year'])
    except:
        b_d = 0
        b_m = 0
        b_y = 0
    digit_check = re.compile(r'.*\d')
    pass_check = re.compile(r'^(?=.*[A-Z])(?=.*\d)')
    email_check = re.compile(r'^[A-Za-z0-9.+_-]+@[a-zA-Z._-]+\.[a-zA-Z]+$')
    fail = False

    for field in [em, na_1, na_2, pwd_1, pwd_2, b_d, b_m, b_y]:
        if len(field) == 0:
            flash("Please fill in all fields!")
            fail = True
            break

    for field in [na_1, na_2]:
        if not digit_check.match(field) is None:
            flash("Your name cannot contain numbers!")
            fail = True
            break

    if pwd_1 == pwd_2:
        if len(pwd_1) < 9:
            flash("Passwords must be at least 9 charachters long!")
            fail = True
        elif pass_check.match(pwd_1) is None:
            flash("Password must contain a CAPITAL and a number.")
            fail = True
    else:
        flash("Passwords do not match!")
        fail = True

    if email_check.match(em) is None:
        flash("Not a real email!")
        fail = True

    
    try:
        user_birth = datetime.datetime(year=b_y, month=b_m, day=b_d)
        if datetime.datetime.today() <= user_birth:
            flash("Be older.")
            fail = True
    except:
        flash("You can't have been bourn on this day.")
        fail = True
            

    if fail:
        return redirect('/')
    else:
        flash("You drove off a cliff, sucsessfully.", 'success')
        return redirect('/')

app.run(debug=True)