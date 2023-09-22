from django.db import models
from django import forms
# Create your models here.

# user form which is later implemented in view.py
class UserForm(models.Model):
    username= models.CharField(max_length=128)
    email= models.EmailField(max_length = 254)
    password1 = forms.CharField(widget=forms.PasswordInput)
    password2 = forms.CharField(widget=forms.PasswordInput)
    