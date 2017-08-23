from django.shortcuts import render
from ..login_app.models import User

# Create your views here.
def display_all(req):
    context = {
        'months' : [],
    }
    for i in range(1,13):
        month = User.objects.filter(birthday__month=i).order_by('birthday')
        context['months'].append(month)
    print context['months']
    return render(req, 'views_app/all.html', context)