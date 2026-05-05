from django.urls import path
from . import views

app_name = 'catalog'

urlpatterns = [
    path('', views.catalog, name='catalog'),
    path('toggle-favorite/', views.toggle_favorite, name='toggle_favorite'),
    path('get-likes/', views.get_likes, name="get_likes")
]