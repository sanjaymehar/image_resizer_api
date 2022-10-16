from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
from .manager import *
from django.dispatch import receiver
import os

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
    
    
@receiver(models.signals.post_delete, sender=Eimage)
def auto_delete_file_on_delete(sender, instance, **kwargs):
    if instance.gray:
        if os.path.isfile(instance.gray.path):
            os.remove(instance.gray.path)

    if instance.thumbnail:
        if os.path.isfile(instance.thumbnail.path):
            os.remove(instance.thumbnail.path)

    if instance.medium:
        if os.path.isfile(instance.medium.path):
            os.remove(instance.medium.path)

    if instance.large:
        if os.path.isfile(instance.large.path):
            os.remove(instance.large.path)

@receiver(models.signals.post_delete, sender=Imagee)
def auto_delete_file_on_delete(sender, instance, **kwargs):
    if instance.image:
        if os.path.isfile(instance.image.path):
            os.remove(instance.image.path)
        
