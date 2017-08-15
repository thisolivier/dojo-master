from django import forms

class UserForm(forms.Form):
    first_name = forms.CharField(max_length=255, label="First Name")
    last_name = forms.CharField(max_length=255, label="Last Name")
    email = forms.CharField(max_length=255, label="Email")
    user_id = forms.IntegerField(widget=forms.HiddenInput(), initial=-1)