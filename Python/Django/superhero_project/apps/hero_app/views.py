from django.shortcuts import render, redirect
from models import Power, Hero

# Create your views here.
def power_form(req):
    context = {
        'names' : Power.objects.all().values('name'),
    }
    return render(req, 'hero_app/add_power.html', context)

def add_power(req):
    # check fields
    results = Power.objects.validate_power(req.POST)
    check_results(results, req)

    if len(Power.objects.filter(name=req.POST['name'])) != 0:
        messages.error(req, 'Power already exists #happysad')
        return redirect('/hero/power')
    
    # create power
    power = Power()
    power.name = req.POST['name']
    power.description = req.POST['description']
    power.save()
    print "----> New power added:", power.name
    return redirect('/home')

def hero_form(req):
    context = {
        'names' : Hero.objects.all().values('name'),
    }
    return render(req, 'hero_app/add_hero.html', context)

def add_hero(req):
    # check fields
    if req.POST['name'] < 3:
        messages.error(req, 'Hero name too short')
        return redirect('/hero/hero')

    if len(Power.objects.filter(name=req.POST['name'])) != 0:
        messages.error(req, 'Hero already exists #happysad')
        return redirect('/hero/hero')
    
    # create hero
    hero = Hero()
    hero.name = req.POST['name']
    hero.save()
    print "----> New hero added:", hero.name
    return redirect('/hero/view_hero/{}'.format(hero.id))

def check_results(results, req):
    failed = False
    for key in results:
        if results[key] != True:
            failed = True
            messages.error(req, 'There was a problem with your {}; {}'.format(key, results[key][1]))
    
    return failed

def view_hero(req, target):
    hero = Hero.objects.get(id=target)
    powers = Power.objects.all()
    
    context = {
        'hero_name' : hero.name,
        'hero_id': hero.id,
        'hero_powers' : hero.powers.all(),
        'all_powers' : powers,
    }
    
    return render(req, 'hero_app/view_hero.html', context)

def save_hero(req):
    #Add power
    hero = Hero.objects.get(id=req.POST['hero_id'])
    power = Power.objects.get(id=req.POST['power_id'])

    hero.powers.add(power)
    hero.save()
    print "------> Power of {} added".format(power.name)

    #Redirect
    if 'again' in req.POST:
        return redirect('/hero/view_hero/{}'.format(req.POST['hero_id']))

    else:
        return redirect('/home')