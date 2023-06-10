from django.urls import path

from apps.clients.views import ClientsCreateView, ClientsListView, ClientsUpdateView, ClientsDetailView, \
    ClientsDeleteView

app_name = 'clients'

urlpatterns = [
    path('add_client/', ClientsCreateView.as_view(), name='add_client'),
    path('clients/', ClientsListView.as_view(), name='clients_list'),
    path('client/<int:pk>', ClientsDetailView.as_view(), name='client_detail'),
    path('client/update/<int:pk>', ClientsUpdateView.as_view(), name='client_update'),
    path('client/delete/<int:pk>', ClientsDeleteView.as_view(), name='client_delete')
]
