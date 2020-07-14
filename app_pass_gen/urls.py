from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home, name='home'),
    path('password/',views.password,name='password'),
    path('about/', views.about, name='about')
]
