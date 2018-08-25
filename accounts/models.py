# coding=utf-8

import re

from django.db import models
from django.core import validators
from django.contrib.auth.models import AbstractBaseUser, UserManager, PermissionsMixin


class User(AbstractBaseUser, PermissionsMixin):

    username = models.CharField(
         'Usuário', max_length=30, unique=True, validators=[
            validators.RegexValidator(
                re.compile('^[\w.@+-]+$'),
                'Informe um nome de usuário válido. '
                'Este valor deve conter apenas letras, números '
                'e os caracteres: @/./+/-/_ .'
                , 'invalid'
            )
        ], help_text='Um nome curto que será usado para identificá-lo de forma única na plataforma'
    )
    name = models.CharField('Nome', max_length=100, blank=True)
    cpf = models.CharField('CPF', max_length=11, unique=True)
    email = models.EmailField('E-mail', unique=True)
    telefone = models.CharField('Telefone', max_length=11, blank=True)
    cep = models.CharField('CEP', max_length=11, blank=True)
    city = models.CharField('Cidade', max_length=100)
    adress = models.CharField('Endereço', max_length=150)
    number = models.IntegerField('Nº')
    complement = models.CharField('Complemento', max_length=200)

    is_staff = models.BooleanField('Equipe', default=False)
    is_active = models.BooleanField('Ativo', default=True)
    date_joined = models.DateTimeField('Data de Entrada', auto_now_add=True)


    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['cpf', 'email', 'telefone']

    objects = UserManager()

    class Meta:
        verbose_name = 'Usuário'
        verbose_name_plural = 'Usuários'

    def __str__(self):
        return self.name or self.username

    def get_full_name(self):
        return str(self)

    def get_short_name(self):
        return str(self).split(" ")[0]
