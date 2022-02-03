from user_example.views import special
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('', include('user_example.urls')),
     path('special/', special, name='special'),
]