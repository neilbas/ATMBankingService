from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('', views.change_pin_view, name='changepin'),
    path('', views.login_view, name = 'login'),

]