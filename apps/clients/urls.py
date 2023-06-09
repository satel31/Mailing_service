from django.urls import path

from apps.clients.views import ClientCreateView

urlpatterns = [
    path('add_client/', ClientCreateView.as_view(), name='add_client'),
]
