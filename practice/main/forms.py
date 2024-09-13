from django import forms
from .models import Client, Moihik, Zapisi

class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = ['name', 'email', 'phone']

class MoihikForm(forms.ModelForm):
    class Meta:
        model = Moihik
        fields = ['name', 'email', 'phone']

class ZapisiForm(forms.ModelForm):
    class Meta:
        model = Zapisi
        fields = ['client', 'moihik', 'date', 'service_type']  # Добавлено поле service_type
