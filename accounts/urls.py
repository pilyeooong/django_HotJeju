from django.urls import path
from .views import *

app_name='accounts'

urlpatterns = [
    path('join/',account_join, name='account_join'),
    path('login/',login_check, name='login'),
    path('logout',logout,name='logout'),
]