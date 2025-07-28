from django.contrib import admin

from .models import YoutubeChannel, Video, Subscription

admin.site.register(YoutubeChannel)

admin.site.register(Video)

admin.site.register(Subscription)

