from django.shortcuts import render, redirect
from .models import User
from . import tables
from .forms import UserForm

# Create your views here.

def view_all(req):
    print "--------> Views reached"
    query = User.objects.all()
    context = {
        'table' : tables.table_design( query ),
    }
    return render(req, 'users_app/index.html', context)


def view_single(req, requested_id):
    context = {
        'user' : User.objects.get(id= requested_id)
    }
    return render(req, 'users_app/user.html', context)

def create_edit(req, requested_id = False):
    print "--------> Loading views database inerface with id {}".format(requested_id)
    if requested_id:
        query = User.objects.get(id=requested_id).__dict__
        query['user_id'] = query['id']
        form = UserForm(initial= query)
        title = 'Edit User ID {}'.format(query['id'])
    else:
        title = 'Create User'
        form = UserForm()
    
    context = {
        'form' : form,
        'id' : requested_id,
        'title' : title
    }
    return render(req, 'users_app/edit.html', context)

def save(req, methods=['POST']):
    print '----------> Beginning save'
    form_full = UserForm(req.POST)
    if form_full.is_valid():
        first_name = req.POST['first_name']
        last_name = req.POST['last_name']
        email = req.POST['email']
        new_id = req.POST['user_id']
    if int(new_id) >= 0:
        user = User.objects.get(id=new_id)
    else:
        user = User(first_name = 'Bob')

    user.first_name = first_name
    user.last_name = last_name 
    user.email = email
    user.save()
    
    return redirect('/users/{}'.format(user.id))

def destroy(req, requested_id):
    user = User.objects.get(id=requested_id)
    user.delete()
    return redirect('/users')