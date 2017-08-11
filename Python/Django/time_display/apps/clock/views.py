from django.shortcuts import render
from time import gmtime, strftime

# Create your views here.
def give_time(request):
    print "----> Entered the views, rendering the index from give_time."
    context = {
        "nowTime": strftime("%b %d, %Y %H:%M %p", gmtime()),
    }
    return render(request, 'clock/index.html', context)