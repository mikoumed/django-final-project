from django import forms
from .models import User, Category, Country
from django.contrib.auth.forms import UserCreationForm
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Field
from django.forms import ModelForm


class SignUpForm(UserCreationForm):

    categories = forms.ModelMultipleChoiceField(queryset=Category.objects.all(), widget=forms.CheckboxSelectMultiple(), required=True)
    countries = forms.ModelMultipleChoiceField(queryset=Country.objects.all(), widget=forms.CheckboxSelectMultiple(), required=True)

    class Meta:
        model = User
        fields = ['username', 'email','categories', 'countries',]
    #
    # def get_list_fields(self):
    #     for field_name in self.fields:
    #         if field_name in ['categories', 'countries']:
    #             yield self[field_name]
class UpdateProfileForm(SignUpForm):
    class Meta:
        model = User
        fields = ['categories', 'countries']
