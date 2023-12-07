from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('aa/', include('App1.urls')),
    path('auth/', include('Authentication.urls')),
]
