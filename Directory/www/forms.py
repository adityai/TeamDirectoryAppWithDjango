from django import forms
from .models import Person

class PersonForm(forms.ModelForm):
    class Meta:
        model = Person
        fields = ['name', 'email', 'title', 'image', 'responsibility', 'bio', 'twitter', 'github', 'birthday']

