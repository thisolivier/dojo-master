from django.shortcuts import render

# Create your views here.
def users_all(request):
    print "----> Print all users"
    return render(request, 'users/index.html')

def users_new(request):
    print "----> Make new user"
    return render(request, 'users/index.html')

def users_entry(request, action):
    print "----> Login or Register"
    return render(request, 'users/index.html')