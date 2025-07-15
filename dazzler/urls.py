from django.urls import path
from . import views

urlpatterns = [
    path('', views.landing, name='landing'),
    path('home/', views.home, name='home'),
    path('tour/', views.tour, name='tour'),
    path('merch/', views.merch, name='merch'),
]