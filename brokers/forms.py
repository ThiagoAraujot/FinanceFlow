from django import forms
from . import models


class BrokerForm(forms.ModelForm):

    class Meta:
        model = models.Broker
        fields = ['name', 'description',]

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
        }

        labels = {
            'name': 'Corretora/Banco',
            'description': 'Descrição'
        }
