from django.shortcuts import render

# Create your views here.
def display_log_reg(req):
    return render(req, 'login_reg/login.html')

def process_log(req):
    print "--------> Processing Signin"