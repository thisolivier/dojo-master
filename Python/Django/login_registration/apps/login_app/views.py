from django.shortcuts import render, redirect
from . import forms, models, security

# Create your views here.
def login_page(req):
    print "-------> Login page running"
    context = {
        'form_login' : forms.Login(),
        'form_reg' : forms.Register()
    }
    return render(req, 'login_app/login.html', context)

def login(req):
    form = forms.Register(req.POST)
    if form.is_valid():
        input_email = form.cleaned_data['email']
        input_pw = form.cleaned_data['password']
        associated_user = models.User.objects.get(email= input_email)
        associated_pass = associated_user['password']
        print associated_pass

        logintrue = security.check(input_pw, associated_pass)
        print logintrue
    return redirect('/success')

def register(req):
    form = forms.Register(req.POST)
    if form.is_valid():
        password = form.cleaned_data['password']
        hashed_pw = security.hash(password)
        print hashed_pw;

        new_user = models.User()
        new_user.password = hashed_pw
        new_user.first_name = form.cleaned_data['first_name']
        new_user.last_name = form.cleaned_data['last_name']
        new_user.email_name = form.cleaned_data['email']
        new_user.save()

        return redirect('/success')

def success(req):
    pass