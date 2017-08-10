from django.shortcuts import render

# Create your views here.
def test(request):
    return render(request, 'best_app/index.html')