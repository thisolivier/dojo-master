from django.shortcuts import render
from ..login_reg.models import User
from . import tables

# Create your views here.
def display_home(req):
    print '-------------> display_home(req)'
    user = req.session['user_id']
    user = User.objects.get(id=user)
    query_gold = User.objects.all().order_by('-gold').values()

    context = {
        'golds' : user.gold,
        'top5table' : tables.name_gold(query_gold, 5)
    }
    return render(req, 'meta_display/home.html', context)

def display_all(req):
    print '-------------> display_all(req)'
    query_gold = User.objects.all().order_by('-gold').values()

    context = {
        'toptable' : tables.name_gold(query_gold)
    }
    return render(req, 'meta_display/view_all.html', context)

def inspect_single(req, user_id):
    print '-------------> inspect_single(req, user_id: {})'.format(user_id)
    user = User.objects.get(id=user_id)
    context = {
        'name': user.email,
        'gold': user.gold,
        'user_id': user_id,
        'log': user.log,
    }
    return render(req, 'meta_display/single.html', context)
    pass