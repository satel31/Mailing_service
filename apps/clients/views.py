from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, UpdateView, DeleteView

from apps.clients.models import Clients


# CRUD
class ClientsCreateView(CreateView):
    model = Clients
    fields = ('email', 'name', 'comment',)
    success_url = reverse_lazy('clients:clients_list')

class ClientsListView(ListView):
    model = Clients
    extra_context = {
        'title': 'Your Client List',
    }

    def get_queryset(self):
        return super().get_queryset().order_by('pk')

class ClientsDetailView(DeleteView):
    model = Clients
    template_name = 'clients/clients_detail.html'

    def get_context_data(self, *args, **kwargs):
        context_data = super().get_context_data(**kwargs)
        context_data['title'] = context_data['object'].name
        return context_data
class ClientsUpdateView(UpdateView):
    model = Clients
    fields = ('email', 'name', 'comment',)
    success_url = reverse_lazy('clients:clients_list')

class ClientsDeleteView(DeleteView):
    model = Clients
    success_url = reverse_lazy('clients:clients_list')


