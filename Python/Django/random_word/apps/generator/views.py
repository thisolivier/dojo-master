from django.shortcuts import render, redirect
from django.utils.crypto import get_random_string

# Create your views here.
def gen_root(request):
    print "----> Generator rooting you out"
    
    if "count" not in request.session:
        request.session['count'] = 0
        print "---> starting a count"
    
    context = {
        "random" : get_random_string(length=14),
        "count" : request.session['count'],
    }

    request.session['count'] = context['count'] + 1

    return render(request, 'generator/index.html', context)

def gen_reset(request):
    print "----> Generator resetting the count"
    request.session['count'] = 0
    return redirect('/random_word')