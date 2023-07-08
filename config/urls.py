from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('clients/', include('apps.clients.urls'), name='clients'),
    path('', include('apps.mailings.urls'), name='mailings'),
    path('users/', include('apps.users.urls'), name='users'),
    path('blog/', include('apps.blog.urls'), name='blog'),
]
