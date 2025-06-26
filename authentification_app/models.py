from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images/', blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)


class Telephone(models.Model):
    nom_telephone = models.CharField(max_length=255)