from django.urls import path
from . import views

app_name = 'registration'

urlpatterns = [
    path('', views.registration, name='registration'),
    path('verify_phone_number/', views.verify_phone_number, name='verification_phone'),
]