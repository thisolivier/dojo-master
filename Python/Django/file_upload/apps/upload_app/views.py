from django.shortcuts import render, redirect
from django import forms

# Utilities
class UploadFileForm(forms.Form):
    file = forms.FileField()

def handle_uploaded_file(file, req):
    files = req.session['files']
    files_len = len(req.session['files'])
    files.append({
            'name' : file.name,
            'data' : ""
    })
    mystr= ' '
    for chunk in file.chunks():
        mystr += chunk
    mystr = mystr.decode('ISO-8859-1')
    files[files_len]['data'] = mystr
    req.session.modified = True

def reset(req):
    print "-----> Resetting"
    req.session['files'] = []
    return redirect('/')

# Create your views here.
def upload_form(req):
    print "-------> Rendering Form"
    try:
        req.session['files']
    except:
        reset(req)
    return render(req, 'upload_app/upload.html')

def process_upload(req, methods=['POST']):
    print "-------> Uploading..."
    form = UploadFileForm(req.POST, req.FILES)

    if form.is_valid():
        handle_uploaded_file(req.FILES['file'], req)
        print "------> Upload success"
        return redirect('/')

    print "-------> Upload fail"
    return redirect('/fail')
