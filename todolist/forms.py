from cProfile import label
from django import forms

class todoForm(forms.Form):
    title = forms.CharField(label='Title', max_length=250,required=True)
    description = forms.CharField(label='Description', min_length=10,required=True)