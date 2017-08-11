from django.shortcuts import render
from django.utils.crypto import get_random_string

# Create your views here.
def gen_root(req):
    print "----> Generator rooting you our"
    context = {
        "random" : get_random_string(length=14),
    }
    return render(req, 'generator/index.html', context)