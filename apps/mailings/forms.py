from django import forms

from apps.mailings.models import Mail, Mailings


class StyleFormMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control-10'


class MailForm(StyleFormMixin, forms.ModelForm):
    class Meta:
        model = Mail
        fields = '__all__'
        exclude = ('owner',)


class MailingsForm(StyleFormMixin, forms.ModelForm):
    class Meta:
        model = Mailings
        fields = '__all__'
        exclude = ('status', 'owner',)
