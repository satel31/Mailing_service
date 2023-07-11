from django import forms

from apps.clients.models import Clients, Groups


class StyleFormMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control-10'


class ClientsForm(StyleFormMixin, forms.ModelForm):
    class Meta:
        model = Clients
        fields = '__all__'
        exclude = ('owner', )


class GroupsForm(StyleFormMixin, forms.ModelForm):
    class Meta:
        model = Groups
        fields = '__all__'
        exclude = ('owner',)
