from django.urls import path, include
from network import views
from django.conf.urls.static import static
from . import settings
from django.contrib import admin
from login import views

urlpatterns = [
    path('admin', admin.site.urls),
    path('', include('network.urls')),
    path('feedback/', include('feedback.urls')),
    path('catalog/', include('catalog.urls')),
    path('login/', include('login.urls')),
    path('registration/', include('registration.urls'), name="registration"),
    path('logout/', views.logout_view, name='logout'),


]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)