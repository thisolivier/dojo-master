from django.shortcuts import render, redirect
from forms import UploadFileForm
from models import File

# Utilities
def reset(req):
    print "-----> Resetting"
    req.session['files'] = []
    return redirect('/')

# Create your views here.
def upload_form(req):
    print "-------> Rendering Form"
    context = {
        'form' : UploadFileForm(),
        'files' : File.objects.all(),
    }

    return render(req, 'upload_app/upload.html', context)

def process_upload(req, methods=['POST']):
    print "-------> Uploading..."
    form = UploadFileForm(req.POST, req.FILES)

    if form.is_valid():
        form.save()
        print "------> Upload success"
        return redirect('/')

    print "-------> Upload fail"
    return redirect('/fail')
