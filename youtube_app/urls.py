from django.urls import path

from .views import home, channel, chaine_details, upload


urlpatterns =  [
    path('', home, name='home'),
    path('create/channel/', channel, name='channel'),
    
    path('chaine/details/<int:pk>', chaine_details, name='chaine'),

    path ('upload/<int:pk>', upload, name='upload')

]


