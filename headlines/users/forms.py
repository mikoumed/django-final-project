from django import forms
from .models import User
from django.contrib.auth.forms import UserCreationForm


CHOICES = (
    ('A', 'A'),
    ('B', 'B'),
)
class SignUpForm(UserCreationForm):
    categories = forms.ChoiceField(choices=CHOICES)
    languages = forms.ChoiceField(choices=CHOICES)
    countries = forms.ChoiceField(choices=CHOICES)

    class Meta(UserCreationForm):
        model = User
        fields = ('username', 'email','categories', 'languages', 'countries')
