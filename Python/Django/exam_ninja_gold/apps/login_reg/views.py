from django.shortcuts import render, redirect
from django.contrib import messages
from models import User

# Create your views here.
def display_log_reg(req):
    return render(req, 'login_reg/login.html')

def process_log(req):
    results = User.objects.user_validator(req.POST)
    
    if not results['safe']:
        for message in results['errors']:
            messages.error(req, message, extra_tags=req.POST['form'])
        return redirect('/sign')
    else:
        if req.POST['form'] == 'login':
            login_results = User.objects.user_login(results['safe_email'], req.POST['password'])
            if not login_results['success']:
                messages.error(req, message, extra_tags=req.POST['form'])
                return redirect('/sign')
            else:
                messages.success(req, 'You logged in!', extra_tags=req.POST['form'])
                req.session['user_id'] = login_results['user_id']
                return redirect('/meta')

        elif req.POST['form'] == 'register':
            User.objects.create(email=results['safe_email'], password=results['safe_password'])
            req.session['user_id'] = User.objects.last().id
            messages.success(req, 'Did it!', extra_tags=req.POST['form'])
        return redirect('/meta')