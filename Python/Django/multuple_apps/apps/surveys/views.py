from django.shortcuts import render

# Create your views here.
def surveys_root(request):
    print "---> Survey root"
    return render(request, 'surveys/index.html')

def surveys_new(request):
    print "---> New survey"
    return render(request, 'surveys/index.html')