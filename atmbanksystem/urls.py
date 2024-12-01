from django.contrib import admin
from django.urls import path, include
from atmsystem import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home_view, name='home'),
    path('atmsystem/', include('atmsystem.urls')),
    path('login/', views.login_view, name='login'),
    path('signup/', views.signup_view, name='signup'),
    path('deposit/', views.deposit_view, name='deposit'),
    path('withdraw/', views.withdraw_view, name='withdraw'),
    path('sendmoney/', views.send_money_view, name='send_money'),
    path('changepin/', views.change_pin_view, name='changepin'),

]