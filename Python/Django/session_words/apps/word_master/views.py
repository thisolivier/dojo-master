from django.shortcuts import render, redirect
import time

# Create your views here.
def root(req):
    return render(req, 'word_master/index.html')

def process(req):
    print "--------> Beginning stuff"
    """ Make a new string """
    try:
        size = req.POST['big']
    except:
        size = 'normal'
    color = req.POST['color']
    word = req.POST['word']
    timeStamp = time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime())
    newString = '<li class="{} {}">{}<span>{}</span></li>'.format(color, size, word, timeStamp)
    

    """ Save string to session """
    try:
        req.session['entries'].append(newString)
        req.session.modified = True
    except:
        print "failing"
        req.session['entries'] = [newString]

    print req.session['entries']
    return redirect('/surveys')

def reset(req):
    try:
        del req.session['entries']
        print "------> Deleted"
    except:
        print "-------> Nothing to delete"
    return redirect('/surveys')