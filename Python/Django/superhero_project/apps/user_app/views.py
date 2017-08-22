from django.shortcuts import render, redirect
from ..hero_app.models import Hero
from ..login_app.models import User

# Create your views here.
def show_all(req):
    if not 'user_id' in req.session:
        return redirect('/portal')

    context = {
        'user_id' : req.session['user_id'],
        'heros_query' : Hero.objects.all(),
        'user' : User.objects.get(id=req.session['user_id'])
    }
    # User.objects.get(id=req.session['user_id'])
    return render(req, 'user_app/index.html', context)
    
def like_hero(req, target):
    print "---------> Time to like"
    hero = Hero.objects.get(id=target)
    print hero.name
    user = User.objects.get(id=req.session['user_id'])
    hero.liked_by.add(user)
    hero.save()
    return redirect('/home')

def hate_hero(req, target):
    print "---------> Time to hate"
    hero = Hero.objects.get(id=target)
    print hero.name
    user = User.objects.get(id=req.session['user_id'])
    hero.liked_by.remove(user)
    hero.save()
    return redirect('/home')