from django.contrib import admin
from django.urls import path, include
from crud import settings

urlpatterns = [
    path('', include('crudapp.urls')),
    path('users/', include('users.urls', namespace='users')),
    # path('users/', include('django.contrib.auth.urls')),
    path('admin/', admin.site.urls),
]
if settings.DEBUG:
    import debug_toolbar

    urlpatterns += [
        path('__debug__/', include(debug_toolbar.urls)),
    ]
