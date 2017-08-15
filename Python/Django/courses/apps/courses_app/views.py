from django.shortcuts import render, redirect
from . import forms, tables
from models import Course

# Create your views here.
def show_all(req):
    print "------> rendering data"
    data = Course.objects.all()
    print data.values()
    table = tables.course_table(data)
    form = forms.CourseForm
    context = {
        'form' : form,
        'table' : table
    }
    return render(req, 'courses_app/index.html', context)

def add(req):
    form = forms.CourseForm(req.POST)
    if form.is_valid() and len(req.POST['name']) > 5 and len(req.POST['desc']) > 15:
        print "-------> form is valid"
        Course.objects.create(name = req.POST['name'], desc = req.POST['desc'])
    return redirect('/')

def confirm(req, course_id):
    course = Course.objects.get(id=course_id)
    context = {
        'course' : course
    }
    return render(req, 'courses_app/confirm.html', context)

def destroy(req, course_id):
    course = Course.objects.get(id=course_id)
    course.delete()
    return redirect('/')