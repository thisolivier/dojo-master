from django.shortcuts import render, redirect
from django.contrib import messages
from models import User
from . import forms
import bcrypt

# Create your views here.
def login_page(req):
    print "-------> Login page running"
    context = {
        'form_reg' : forms.register(),
        'form_log' : forms.login()
    }
    return render(req, 'login_app/login.html', context)

def register(req):
    results = User.objects.check_reg(req.POST)
    if results['status']:
        new_user = User()
        new_user.first_name = req.POST['first_name']
        new_user.last_name = req.POST['last_name']
        new_user.email = req.POST['email']
        new_user.password = bcrypt.hashpw(req.POST['password'].encode(), bcrypt.gensalt())
        new_user.save()
        messages.success(req, 'Wee, new user created! Please login.', extra_tags='register')
    else:
        for message in results['errors']:
            messages.error(req, message, extra_tags='register')
    print results
    return redirect('/login')

def login(req):
    results = User.objects.check_login(req.POST)
    if results['status']:
        messages.success(req, 'Congratulations, you user you!', extra_tags='login')
    else:
        for message in results['errors']:
            messages.error(req, message, extra_tags='login')
    print results
    return redirect('/login')