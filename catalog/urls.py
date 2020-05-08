from django.urls import path
from . import views
from django.urls import include


urlpatterns = [
    path('', views.accueil, name='accueil'),
    path('inscription/', views.renew_inscription, name='inscription'),
    path('commande/', views.commander, name='commande'),
    path('user_login/',views.user_login,name='user_login'),
]

