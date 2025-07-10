from django.db import models

from django.contrib.auth.models import User

# Create your models here.

class YoutubeChannel(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=25)
    description = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='channel_image/', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)



class Video(models.Model):
    titre = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    video = models.FileField(upload_to='videos/', blank=True,null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    channel = models.ForeignKey(YoutubeChannel, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

