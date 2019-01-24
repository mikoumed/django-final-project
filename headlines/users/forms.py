from django import forms
from .models import User, Category, Language
from django.contrib.auth.forms import UserCreationForm
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Field
from django.forms import ModelForm


CHOICES = (
    ('A', 'A'),
    ('B', 'B'),
)
class SignUpForm(UserCreationForm, forms.ModelForm):

    categories = forms.ModelMultipleChoiceField(queryset=Category.objects.all(), widget=forms.CheckboxSelectMultiple(), required=True)
    languages = forms.ModelMultipleChoiceField(queryset=Language.objects.all(), widget=forms.CheckboxSelectMultiple(), required=True)

    class Meta:
        model = User
        fields = ['username', 'email','categories', 'languages',]
    #
    # def get_list_fields(self):
    #     for field_name in self.fields:
    #         if field_name in ['categories', 'countries']:
    #             yield self[field_name]
