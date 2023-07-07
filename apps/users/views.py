from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView

from apps.users.forms import RegisterForm, ActivationForm, UserProfileForm
from apps.users.models import User
from apps.users.services import send_email


class RegisterView(CreateView):
    model = User
    form_class = RegisterForm
    template_name = 'users/register.html'
    success_url = reverse_lazy('users:login')

    def form_valid(self, form):
        if form.is_valid():
            self.object = form.save()
            self.object.activation_code = User.objects.make_random_password()
            self.object.save()
            send_email(self.object.activation_code, self.object.email, self.object.id)
        return super().form_valid(form)

class ActivationView(UpdateView):
    model = User
    form_class = ActivationForm
    template_name = 'users/activation.html'
    success_url = reverse_lazy('mailings:mailings')

    #def get_success_url(self):
        #if self.request.user.is_authenticated:
            #url = reverse('catalog:products')
        #else:
            #url = reverse('users:login')
        #return url

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        ver_code = self.request.GET.get('code', '')
        kwargs.update({'initial': {'user_code': ver_code}})
        return kwargs

    def form_valid(self, form):
        if self.request.method == 'POST':
            user_code = self.request.POST.get('user_code')
            self.object = form.save()
            if user_code == self.object.activation_code:
                self.object.is_activated = True
                self.object.save(update_fields=['is_activated'])
                return super().form_valid(form)
            else:
                form.add_error('user_code', 'Invalid code')
                return super().form_invalid(form)

class ProfileView(UpdateView):
    model = User
    form_class = UserProfileForm
    success_url = reverse_lazy('mailings:mailings')

    def get_object(self, queryset=None):
        return self.request.user