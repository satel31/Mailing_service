from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, UpdateView, DeleteView, DetailView

from apps.mailings.forms import MailForm, MailingsForm
from apps.mailings.models import Mail, Mailings, MailingLog
from apps.mailings.services import send_mailing


class MailCreateView(CreateView):
    model = Mail
    form_class = MailForm
    success_url = reverse_lazy('mailings:mails')


class MailListView(ListView):
    model = Mail
    extra_context = {
        'title': 'Your Mails'
    }


class MailUpdateView(UpdateView):
    model = Mail
    form_class = MailForm
    success_url = reverse_lazy('mailings:mails')


class MailDeleteView(DeleteView):
    model = Mail
    success_url = reverse_lazy('mailings:mails')


class MailingsCreateView(CreateView):
    model = Mailings
    form_class = MailingsForm
    success_url = reverse_lazy('mailings:mailings')

    def form_valid(self, form):
        self.object = form.save()
        send_mailing()
        self.object.save()
        return super().form_valid(form)


class MailingsListView(ListView):
    model = Mailings
    extra_context = {
        'title': 'Your Mailings'
    }


class MailingsUpdateView(UpdateView):
    model = Mailings
    form_class = MailingsForm
    success_url = reverse_lazy('mailings:mailings')

    def form_valid(self, form):
        self.object = form.save()
        send_mailing()
        self.object.save()
        return super().form_valid(form)


class MailingsDeleteView(DeleteView):
    model = Mailings
    success_url = reverse_lazy('mailings:mailings')


class MailingLogListView(ListView):
    model = MailingLog
    extra_context = {
        'title': 'Your History of Mailing'
    }
