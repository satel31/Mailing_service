from django.views.generic import CreateView, ListView

from apps.clients.models import Client


# CRUD
class ClientCreateView(CreateView):
    model = Client
    fields = ('email', 'first_name', 'last_name', 'comment',)
    #success_url = reverse_lazy('clients: all_clients')

class ClientListView(ListView):
    model = Client
    extra_context = {
        'title': 'Your Client List',
    }


