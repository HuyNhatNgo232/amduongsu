from .models import Webapp
from django import forms

class WebappForm(forms.ModelForm):
    class Meta:
        webapp = Webapp
        fields = ('title')