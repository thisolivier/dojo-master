from django.shortcuts import render, redirect
from django.contrib import messages

from random import getrandbits
from time import strftime, gmtime

from ..login_reg.models import User
from . import tables

# Create your views here.
def display_game(req):
    user = req.session['user_id']
    user = User.objects.get(id=user)

    context = {
        'golds' : user.gold,
        'top5table' : "boo",
        'log' : str(user.log).split('#')
    }
    return render(req, 'game/world.html', context)

def proccess_fight(req, opponent):
    print "-------> Fight over, {} was fought".format(opponent)
    # Initialise function
    mini_db = {
        'tree' : 50,
        'hulk' : 1000,
        'pants' : 5,
        'plant' : 1,
    }
    risk = mini_db[opponent]
    win = getrandbits(1)
    if not win:
        win = -1
    user = User.objects.get(id=req.session['user_id'])

    # Work out new values
    newgold = user.gold + (risk * win)
    timestamp = strftime("%Y-%m-%d %H:%M:%S", gmtime())
    log_entry = "{} | {} played <b>{}</b> | Result of {}".format(str(timestamp), user.email, opponent, (risk * win))

    # Maybe kill user
    if (newgold < 0):
        #user.delete()
        messages.error(req, 'You were eaten as payment for loosing, game over.', extra_tags='death')
        return redirect('/sign')

    # Save data
    add_log(user, log_entry)
    user.gold = newgold
    user.save()

    return redirect('/game')

def add_log(user, log_entry):
    log_list = str(user.log).split('#')
    log_list.append(log_entry)
    newlog = '#'.join(log_list)
    user.log = newlog
    user.save()

    