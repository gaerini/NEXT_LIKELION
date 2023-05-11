from django.urls import path
from accounts import views

app_name = 'accounts'
urlpatterns = [
# /accounts/s
    path('', views.home, name = 'home'),
]