from django.urls import path

from apps.clients.views import ClientsCreateView, ClientsListView, ClientsUpdateView, ClientsDetailView, \
    ClientsDeleteView, GroupsCreateView, GroupsListView, GroupsUpdateView, GroupsDeleteView

app_name = 'clients'

urlpatterns = [
    # clients urls
    path('add_client/', ClientsCreateView.as_view(), name='add_client'),
    path('<int:pk>/clients/', ClientsListView.as_view(), name='clients_list'),
    path('client/<int:pk>', ClientsDetailView.as_view(), name='client_detail'),
    path('client/update/<int:pk>', ClientsUpdateView.as_view(), name='client_update'),
    path('client/delete/<int:pk>', ClientsDeleteView.as_view(), name='client_delete'),

    # groups urls
    path('add_group/', GroupsCreateView.as_view(), name='add_group'),
    path('groups/', GroupsListView.as_view(), name='groups_list'),
    path('groups/update/<int:pk>', GroupsUpdateView.as_view(), name='groups_update'),
    path('groups/delete/<int:pk>', GroupsDeleteView.as_view(), name='groups_delete'),

]
