# myproject/urls.py

from django.contrib import admin 
from django.urls import path, include


urlpatterns = [
    path('store/', include(('store.urls', 'store'), namespace='store')),
    path('admin/', admin.site.urls),
    
]