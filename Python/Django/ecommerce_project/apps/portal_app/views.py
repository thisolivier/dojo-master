from django.shortcuts import render

# Create your views here.
def render_page(req):
    return render(req, 'portal_app/index.html')