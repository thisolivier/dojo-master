from django.shortcuts import render, redirect
from django.contrib import messages
from ..login_reg.models import User
from . import tables

# Create your views here.
def main_dash(req):
    print "----------> Main dashboard reached"
    user = User.objects.get(id=req.session['user_id'])
    context = {
        'table' : tables.all_table(user.admin),
    }
    return render(req, 'dashboard/view_all.html', context)
    

def edit_user(req, target = False):
    print "---------> Trying to edit user"
    check_access(req) #checks we're logged in, redirects to login if not
    context = {
    }

    #######################################
    #   If user is editing own profile    
    #   If user is editing another profile   
    #   - Check if is admin rights              
    #######################################
    if not target:
        user = User.objects.get(id=req.session['user_id'])
        context['title'] = 'Edit Your Profile'
        context['target_user'] = False
    else:
        if check_access(req, True):
            user = User.objects.get(id=target)
            context['title'] = 'Edit user #{}'.format(target) 
            context['target_user'] = int(target)
        else :
            return redirect('/dashboard') 
        
    
    if check_access(req, True):
        context['dash_link'] = '/admin'

    return render(req, 'dashboard/edit_user.html', context)

def check_access(req, admin_req = False):
    if req.session['user_id']:
        logged_user = User.objects.get(id=req.session['user_id'])
        if admin_req:
            if logged_user.admin:
                return True
            else:
                messages.error(req, 'You need to be an admin to visit that page')
                return False
        else: 
            return True
    messages.error(req, 'You need to sign in to view that page')
    return redirect('/signin')

def save_changes(req, target):
    check_access(req)
    if target == "False":
        # We should save the edits to our own profile
        target_user = User.objects.get(id=req.session['user_id'])
    else:
        if check_access(req, True):
            # We should edit the requested user
            target_user = User.objects.get(id=int(target))
        else : 
            # Non admin is trying to access admin functions
            messages.error(req, 'You need to be an admin to do that')
            return redirect('/dashboard')
        
    
    for field in req.POST:
        if field == 'csrfmiddlewaretoken':
            continue
        if req.POST[field]:
            print "-------> Editing", field
            messages.success(req, 'The {} was updated for {}'.format(field, target_user.id))
            setattr(target_user, field, req.POST[field])
    target_user.save()
    return redirect('/dashboard')

def delete_user(req, target):
    if check_access(req, True):
        target_user = User.objects.get(id=target)
        target_user.delete()
        return redirect('/dashboard/admin')
    else:
        messages.error(req, 'You need to be an admin to do that')
        return redirect('/dashboard')