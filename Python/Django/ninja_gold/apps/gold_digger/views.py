from django.shortcuts import render, redirect
from random import uniform
from time import strftime, gmtime

# Create your views here.
def render_world(req):
    try: 
        context = req.session["log"]
    except:
        context = []

    try: 
        gold = req.session["gold"]
    except:
        gold = req.session["gold"] = 0

    return render(req, 'gold_digger/index.html')

def dig4gold(req):
    try:
        miniDB = {
            "bar_nice" : [20, 50],
            "job" : [5, 10],
            "school" : [2, 5],
            "bar_dive" : [-20, 10],
            "shopping" : [-10, -50],
        }

        location = req.POST["location"]
        whereBeen = miniDB[location]
        timenow = strftime("%Y-%m-%d %H:%M:%S", gmtime())
        value = int(uniform(whereBeen[0], whereBeen[1]))
        direction = "earned"
        if value < 0:
            direction = "lost"
        log_entry = "{} - Visited {} and {} {} golds".format(timenow, location, direction, value)
        
        try:
            req.session["log"].insert(0, log_entry)
            req.session.modified = True
        except:
            req.session["log"] = [log_entry]

        print log_entry
        req.session["gold"] += value
    except:
        print "-----> Route fail"

    return redirect('/')

def reset(req):
    req.session.flush()
    return redirect('/')