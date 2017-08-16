from django import forms

class Register(forms.Form):
    first_name = forms.CharField(max_length = 255)
    last_name = forms.CharField(max_length = 255)
    email = forms.CharField(max_length = 255)
    password = forms.CharField(max_length = 255)

class Login(forms.Form):
    email = forms.CharField(max_length = 255)
    password = forms.CharField(max_length = 255)