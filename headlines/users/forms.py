from django import forms
from .models import User
from django.contrib.auth.forms import UserCreationForm
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Field
from django.forms import ModelForm


CHOICES = (
    ('A', 'A'),
    ('B', 'B'),
)
class SignUpForm(UserCreationForm, ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email','categories', 'languages']
    #
    # def get_list_fields(self):
    #     for field_name in self.fields:
    #         if field_name in ['categories', 'countries']:
    #             yield self[field_name]
