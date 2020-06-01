from django.contrib import admin
from django.urls import path, include

from my_app import views


urlpatterns = [
    
    path("", include("my_app.urls")),
    path('admin/', admin.site.urls),
]
