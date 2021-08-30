from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms 

from .models import Customer


class CustomerForm(ModelForm):
    class meta:
        model = Customer
        fields = '__all__'


class createUserForm(UserCreationForm):
    class meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']