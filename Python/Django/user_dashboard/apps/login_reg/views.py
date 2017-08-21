from django.shortcuts import render, redirect
from django.contrib import messages
from models import User
import bcrypt

# Create your views here.
def register(req):
    context = {
        'title': 'Register',
        'action': '/process_reg',
        'form_fields':"""<div class class="form-group">
                <label for="first_name">First Name</label>
                <input class="form-control" type="text" name="first_name">
            </div>
            <div class class="form-group">
                <label for="first_name">Last Name</label>
                <input class="form-control" type="text" name="last_name">
            </div>
            <div class class="form-group">
                <label for="first_name">Email</label>
                <input class="form-control" type="text" name="email">
            </div>
            <div class class="form-group">
                <label for="first_name">Password</label>
                <input class="form-control" type="password" name="password">
            </div>
            <div class class="form-group">
                <label for="first_name">Confirm Password</label>
                <input class="form-control" type="password" name="password_c">
            </div>"""
    }
    return render(req, 'login_reg/gateway.html', context)

def process_reg(req):
    print '-------------> Processing form'
    results = User.objects.validate_user(req.POST)
    failed = False
    for key in results:
        if results[key] != True:
            failed = True
            problem = results[key][1]
            messages.error(req, 'There was a problem with your {}; {}'.format(key, problem))
    
    if failed: 
        return redirect('/register')

    if not len(User.objects.filter(email=req.POST['email'])) == 0:
        messages.error(req, 'There was a problem with your email; already registered')
        return redirect('/register')
    
    print "-------> Building User"
    new_user = User()
    new_user.first_name = req.POST['first_name']
    new_user.last_name = req.POST['last_name']
    new_user.email = req.POST['email']
    new_user.password = bcrypt.hashpw(req.POST['password'].encode(), bcrypt.gensalt())
    print "-------> Creating User"
    new_user.save()
    messages.success(req, 'New user created! Login to continue.')
    return redirect('/signin')

def sign_in(req):
    context = {
        'title': 'Sign In',
        'footer': True,
        'action': 'process_in',
        'form_fields':"""<div class class="form-group">
                <label for="first_name">Email</label>
                <input class="form-control" type="text" name="email">
            </div>
            <div class class="form-group">
                <label for="first_name">Password</label>
                <input class="form-control" type="password" name="password">
            </div>"""
    }
    return render(req, 'login_reg/gateway.html', context)

def process_in(req):
    print '-------------> Processing Signin'
    results = User.objects.validate_signin(req.POST)
    failed = False
    print results
    for key in results:
        if results[key] != True:
            failed = True
            field_name = str(key).replace('_', ' ')
            problem = results[key][1]
            messages.error(req, 'There was a problem with your {}; {}'.format(field_name, problem))
    
    if failed: 
        return redirect('/signin')
    
    user_query = User.objects.filter(email=req.POST['email'])
    if len(user_query) == 0:
        messages.error(req, 'That email has not been registered.')
        return redirect('/signin')
    elif len(user_query) > 1:
        messages.error(req, 'You are registered twice in our system. Go and never return.')
        return redirect('/signin')

    user = User.objects.get(email=req.POST['email'])
    cannon_pass = user.password
    maybe_pass = req.POST['password']
    is_match = bcrypt.checkpw(maybe_pass.encode(), cannon_pass.encode())
    req.session['user_id'] = user.id

    if user.admin:
        return redirect('/dashboard/admin')
    else:
        return redirect('/dashboard')
    
def process_out(req):
    del req.session['user_id']
    messages.success(req, 'Everybody leaves me, and now you.')
    return redirect('/signin')