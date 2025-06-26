from django.urls import path
from .views import signup, login, logout_user, profile, connection

urlpatterns = [
    path('signup/', signup, name='signup'),
    path('login/', login, name='login'),
    path ('logout/', logout_user, name='logout'),

    path('profile/', profile, name="profile"),

    path('connexion/', connection, name="connexion" )




]