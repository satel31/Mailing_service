from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, UpdateView, DeleteView, DetailView

from apps.clients.forms import GroupsForm, ClientsForm
from apps.clients.models import Clients, Groups


# CRUD
class ClientsCreateView(CreateView):
    model = Clients
    form_class = ClientsForm
    success_url = reverse_lazy('clients:groups_list')


class ClientsListView(ListView):
    model = Clients

    def get_queryset(self):
        queryset = super().get_queryset().filter(group_id=self.kwargs.get('pk')).order_by('pk')
        return queryset

    def get_context_data(self, *args, **kwargs):
        context_data = super().get_context_data(**kwargs)
        groups = Groups.objects.get(pk=self.kwargs.get('pk'))
        context_data['title'] = f'Clients from the group {groups.group_name}'
        return context_data


class ClientsDetailView(DetailView):
    model = Clients
    template_name = 'clients/clients_detail.html'

class ClientsUpdateView(UpdateView):
    model = Clients
    form_class = ClientsForm
    success_url = reverse_lazy('clients:groups_list')


class ClientsDeleteView(DeleteView):
    model = Clients
    success_url = reverse_lazy('clients:groups_list')


class GroupsCreateView(CreateView):
    model = Groups
    form_class = GroupsForm
    success_url = reverse_lazy('clients:groups_list')


class GroupsListView(ListView):
    model = Groups
    extra_context = {
        'title': 'Your Groups'
    }

class GroupsUpdateView(UpdateView):
    model = Groups
    form_class = GroupsForm
    success_url = reverse_lazy('clients:groups_list')

class GroupsDeleteView(DeleteView):
    model = Groups
    success_url = reverse_lazy('clients:groups_list')
