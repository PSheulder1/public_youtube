from django.urls import path

from .views import home, channel, chaine_details, upload, banner, studio


urlpatterns =  [
    path('', home, name='home'),
    path('create/channel/', channel, name='channel'),
    
    path('chaine/details/<int:pk>', chaine_details, name='chaine'),

    path ('upload/<int:pk>', upload, name='upload'),

    path('banner/<int:pk>', banner , name='banner'),

    path('youtube-studio/<int:pk>', studio, name='youtube-studio')

]


