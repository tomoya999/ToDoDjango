from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('crudapp.urls')),
    path('users/', include('users.urls', namespace='users')),
    path('users/', include('django.contrib.auth.urls')),
    path('admin/', admin.site.urls),

]
