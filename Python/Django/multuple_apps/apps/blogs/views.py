from django.shortcuts import render

# Create your views here.
def blog_root(request):
    print "---> Generating root template"
    return render(request, 'blogs/index.html')

def blog_new(request):
    print "---> Generating new blog template"
    return render(request, 'blogs/index.html')

def blog_create(request):
    print "---> Generating create blog template"
    return render(request, 'blogs/index.html')

def blog_num(request, number):
    print "---> Generating create blog number {}".format(number)
    return render(request, 'blogs/index.html')

def blog_modify(request, number, action):
    print "---> Generating {}ing template for blog number {}".format(action, number)
    return render(request, 'blogs/index.html')