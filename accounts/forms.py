# coding=utf-8

from django.contrib.auth.forms import UserCreationForm
from django import forms

from .models import User


class UserAdminCreationForm(UserCreationForm):

    class Meta:
        model = User
        fields = ['username', 'cpf', 'email', 'telefone', 'cep', 'city', 'adress', 'number', 'complement']


class UserAdminForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ['username', 'cpf', 'email', 'name', 'telefone', 'cep', 'city', 'adress', 'number', 'complement', 'is_active', 'is_staff']
