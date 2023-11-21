from django import forms
from .models import MOVIE

class MovieForm(forms.ModelForm):
    class Meta:
        model=MOVIE
        fields=['name','desc','year','img']
