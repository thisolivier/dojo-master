from django.shortcuts import render, redirect

# Create your views here.
def test(req):
    return render(req, 'form/index.html')

def process(req):
    req.session['count'] = 0
    try:
        req.session['count']
    except:
        req.session['count'] = 0
    
    req.session['field'] = req.POST['field']
    req.session['option'] = req.POST['options']
    req.session['comment'] = req.POST['comment']
    req.session['count'] += 1

    print "--------> Form Results ",req.session['result']
    return redirect('/result')

def result(req):
    return render(req, 'form/results.html')