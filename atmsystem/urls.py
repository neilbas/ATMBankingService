from django.urls import path
from . import views

urlpatterns = [
    path('changepin/', views.change_pin_view, name='changepin'),
    path('login/', views.login_view, name='login'),
    path('deposit/', views.deposit_view, name='deposit'),
    path('sendmoney/', views.send_money_view, name='sendmoney'),
    path('withdraw/', views.withdraw_view, name='withdraw'),
    path('signup/', views.signup_view, name='signup'),
]