from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
from .manager import *


class User(AbstractUser):
    username = None
    email = models.EmailField(_('email address'), unique=True)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

class Imagee(models.Model):
    image=models.ImageField(upload_to='images')

class Eimage(models.Model):
    orignal=models.ForeignKey(Imagee,on_delete=models.CASCADE)
    gray=models.ImageField(upload_to='images')
    thumbnail=models.ImageField(upload_to='images')
    medium=models.ImageField(upload_to='images')
    large=models.ImageField(upload_to='images')