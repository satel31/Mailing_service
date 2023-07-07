from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django import forms

from apps.users.models import User


class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('email', 'password1', 'password2',)

class ActivationForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ()

    user_code = forms.CharField(max_length=50, label='Enter verification code')

class UserProfileForm(UserChangeForm):
    class Meta:
        model = User
        fields = ('email',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['password'].widget = forms.HiddenInput()
