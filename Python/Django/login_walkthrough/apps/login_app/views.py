from django.shortcuts import render, redirect
from django.contrib import messages
from models import User

# Create your views here.
def index(req):
    return render(req, 'login_app/index.html')

def register(req):
    results = User.objects.regVal(req.POST)
    if results['status'] == False:
        for error in results['errors']:
            messages.error(req, error)
        return redirect('/')
    user = User.objects.creator(req.POST)
    messages.success(req, 'User has been created, login fool!')
    return redirect('/')

def login(req):
    print "-------> Logging in"
    results = User.objects.logVal(req.POST)
    if results['status'] == False:
        for error in results['errors']:
            messages.error(req, error)
        return redirect('/')
    messages.success(req, 'Ugh, you again!')
    req.session['name'] = results['user'].f_name
    return redirect('/congrats')

def useless(req):
    return render(req, 'login_app/congrats.html')