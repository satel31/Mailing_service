from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, UpdateView, DeleteView, DetailView

from apps.clients.forms import GroupsForm, ClientsForm
from apps.clients.models import Clients, Groups


# CRUD
class ClientsCreateView(LoginRequiredMixin, CreateView):
    model = Clients
    form_class = ClientsForm
    success_url = reverse_lazy('clients:groups_list')

    def form_valid(self, form):
        self.obj = form.save()
        self.object.owner = self.request.user
        self.object.save()
        return super().form_valid(form)


class ClientsListView(LoginRequiredMixin, ListView):
    model = Clients

    def get_queryset(self):
        """Sort by pk"""
        queryset = super().get_queryset().filter(group_id=self.kwargs.get('pk')).order_by('pk')
        if not self.request.user.is_superuser:
            queryset = queryset.filter(owner=self.request.user)
        return queryset

    def get_context_data(self, *args, **kwargs):
        """Add group name to context data"""
        context_data = super().get_context_data(**kwargs)
        groups = Groups.objects.get(pk=self.kwargs.get('pk'))
        context_data['title'] = f'Clients from the group {groups.group_name}'
        return context_data


class ClientsDetailView(LoginRequiredMixin, DetailView):
    model = Clients
    template_name = 'clients/clients_detail.html'

    def get_queryset(self):
        """Sort by pk"""
        queryset = super().get_queryset()
        if not self.request.user.is_superuser:
            queryset = queryset.filter(owner=self.request.user)
        return queryset


class ClientsUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Clients
    form_class = ClientsForm
    success_url = reverse_lazy('clients:groups_list')

    def test_func(self):
        return self.request.user == self.get_object().owner


class ClientsDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Clients
    success_url = reverse_lazy('clients:groups_list')

    def test_func(self):
        return self.request.user == self.get_object().owner


class GroupsCreateView(LoginRequiredMixin, CreateView):
    model = Groups
    form_class = GroupsForm
    success_url = reverse_lazy('clients:groups_list')

    def form_valid(self, form):
        self.obj = form.save()
        self.object.owner = self.request.user
        self.object.save()
        return super().form_valid(form)


class GroupsListView(LoginRequiredMixin, ListView):
    model = Groups
    extra_context = {
        'title': 'Your Groups'
    }

    def get_queryset(self):
        """Sort by pk"""
        queryset = super().get_queryset()
        if not self.request.user.is_superuser:
            queryset = queryset.filter(owner=self.request.user)
        return queryset


class GroupsUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Groups
    form_class = GroupsForm
    success_url = reverse_lazy('clients:groups_list')

    def test_func(self):
        return self.request.user == self.get_object().owner


class GroupsDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Groups
    success_url = reverse_lazy('clients:groups_list')

    def test_func(self):
        return self.request.user == self.get_object().owner
