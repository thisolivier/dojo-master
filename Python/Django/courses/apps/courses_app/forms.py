from django import forms

class CourseForm(forms.Form):
    name = forms.CharField(max_length=255)
    desc = forms.CharField( max_length=20000, widget=forms.Textarea )