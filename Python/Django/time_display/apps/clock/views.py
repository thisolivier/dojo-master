from django.shortcuts import render
from time import gmtime, strftime

# Create your views here.
def give_time(request):
    print "----> Entered the views, rendering the index from give_time."
    context = {
        "nowTime": strftime("%Y-%m-%d %H:%M %p and %S seconds", gmtime()),
    }
    return render(request, 'clock/index.html', context)