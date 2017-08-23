from django.shortcuts import render, redirect
from django.contrib import messages
import pytz
from models import User

# Create your views here.
def display_portal(req):
    return render(req, 'login_app/portal.html')

def process_login(req):
    results = User.objects.validator(req.POST)
    failed = False

    for result in results:
        if not results[result][0]:
            messages.error(req, 'There was a problem with your {}, {}'.format(result, results[result][1]))
            failed = True
    if failed:
        return redirect('/')

    email_matches = User.objects.filter(email=req.POST['email'])
    if not len(email_matches) == 0:
        messages.error(req, 'We already have an entry with that email, first name of {}'.format(email_matches[0].name))
        return redirect('/')

    new_user = User()
    new_user.first_name = req.POST['first_name']
    new_user.last_name = req.POST['last_name']
    new_user.email = req.POST['email']
    new_user.birthday = pytz.utc.localize(results['birthday'][1])
    new_user.save()
    messages.success(req, 'Your entry was added to the database, <a href="/view/all">check it out!</a>')
    return redirect('/')