from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, UpdateView, DeleteView, DetailView, TemplateView

from apps.blog.models import Post
from apps.clients.models import Clients
from apps.mailings.forms import MailForm, MailingsForm
from apps.mailings.models import Mail, Mailings, MailingLog
from apps.mailings.services import send_mailing


class HomePageView(TemplateView):
    template_name = 'mailings/home.html'

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        context_data['count_mailings_all'] = Mailings.objects.all().count()
        context_data['count_mailings_active'] = Mailings.objects.filter(status__in=['created', 'running']).count()
        context_data['count_clients'] = Clients.objects.distinct().count()
        context_data['blog'] = Post.objects.filter(is_published=True).order_by('?')[:3]
        return context_data
class MailCreateView(LoginRequiredMixin, CreateView):
    model = Mail
    form_class = MailForm
    success_url = reverse_lazy('mailings:mails')

    def form_valid(self, form):
        """Adds owner of the mail"""
        self.obj = form.save()
        self.object.owner = self.request.user
        self.object.save()
        return super().form_valid(form)


class MailListView(LoginRequiredMixin, ListView):
    model = Mail
    extra_context = {
        'title': 'Your Mails'
    }

    def get_queryset(self):
        """Sort by pk, filter by owner"""
        queryset = super().get_queryset()
        if not self.request.user.is_superuser:
            queryset = queryset.filter(owner=self.request.user)
        return queryset


class MailUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Mail
    form_class = MailForm
    success_url = reverse_lazy('mailings:mails')

    def test_func(self):
        return self.request.user == self.get_object().owner


class MailDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Mail
    success_url = reverse_lazy('mailings:mails')

    def test_func(self):
        return self.request.user == self.get_object().owner


class MailingsCreateView(LoginRequiredMixin, CreateView):
    model = Mailings
    form_class = MailingsForm
    success_url = reverse_lazy('mailings:mailings')

    def form_valid(self, form):
        """Adds owner of the mail, sends the first email"""
        self.object = form.save()
        self.object.owner = self.request.user
        send_mailing()
        self.object.save()
        return super().form_valid(form)


class MailingsListView(LoginRequiredMixin, ListView):
    model = Mailings
    extra_context = {
        'title': 'Your Mailings'
    }

    def get_queryset(self):
        """Sort by pk, filter by owner"""
        queryset = super().get_queryset()
        if not self.request.user.is_superuser:
            queryset = queryset.filter(owner=self.request.user)
        return queryset


class MailingsUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Mailings
    form_class = MailingsForm
    success_url = reverse_lazy('mailings:mailings')

    def test_func(self):
        return self.request.user == self.get_object().owner

    def form_valid(self, form):
        """Adds owner of the mail"""
        self.object = form.save()
        send_mailing()
        self.object.save()
        return super().form_valid(form)


class MailingsDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Mailings
    success_url = reverse_lazy('mailings:mailings')

    def test_func(self):
        return self.request.user == self.get_object().owner


class MailingLogListView(LoginRequiredMixin, ListView):
    model = MailingLog
    extra_context = {
        'title': 'Your History of Mailing'
    }

    def get_queryset(self):
        """Sort by pk, filter ny owner of the mail"""
        queryset = super().get_queryset()
        if not self.request.user.is_superuser:
            mailing = Mailings.objects.filter(owner=self.request.user)
            mailing_pk = [mail.pk for mail in mailing]
            # __in in mailing__in filter by list of data
            queryset = queryset.filter(mailing__in=mailing_pk)
        return queryset
