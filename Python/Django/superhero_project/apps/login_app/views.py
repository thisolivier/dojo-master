from django.shortcuts import render, redirect
from django.contrib import messages
import bcrypt
from models import User

# Create your views here.
def portal(req):
    return render(req, 'login_app/portal.html')

def register(req):
    results = User.objects.validate_user(req.POST)
    failed = check_results(results, req)
    if failed:
        return redirect('/portal')

    if not len(User.objects.filter(email=req.POST['email'])) == 0:
        messages.error(req, 'There was a problem with your email; already registered')
        return redirect('/portal')
    
    new_user = User()
    new_user.name = req.POST['name']
    new_user.email = req.POST['email']
    new_user.password = bcrypt.hashpw(req.POST['password'].encode(), bcrypt.gensalt())
    new_user.save()
    messages.success(req, 'New user created! Login to continue.')
    return redirect('/portal')

def signin(req):
    results = User.objects.validate_signin(req.POST)

    failed = check_results(results, req)
    if failed:
        return redirect('/portal')

    email_bad = validate_email(req.POST['email'], req)
    if email_bad:
        return redirect('/portal')

    user = User.objects.get(email=req.POST['email'])
    password_match = bcrypt.checkpw(req.POST['password'].encode(), user.password.encode())
    if password_match:
        req.session['user_id'] = user.id
        return redirect('/')
    else:
        messages.error(req, 'Password do not match')
        return redirect('/portal')

def signout(req):
    del req.session['user_id']
    messages.success(req, 'You signed out')
    return redirect('/portal')

def check_results(results, req):
    failed = False
    for key in results:
        if results[key] != True:
            failed = True
            messages.error(req, 'There was a problem with your {}; {}'.format(key, results[key][1]))
    
    return failed

def validate_email(email_test, req):
    user_query = User.objects.filter(email=email_test)
    if len(user_query) == 0:
        messages.error(req, 'That email has not been registered.')
        return True
    elif len(user_query) > 1:
        messages.error(req, 'You are registered twice in our system. Go and never return.')
        return True
    else:
        return False