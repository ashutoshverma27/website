from django import forms

class details(forms.Form):
    fullname=forms.CharField(label='fullname',max_length=100)
    
