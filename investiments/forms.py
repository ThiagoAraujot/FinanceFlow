from django import forms
from . import models


class InvestimentForm(forms.ModelForm):

    class Meta:
        model = models.Investiment
        fields = ['name', 'amount', 'broker',]

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'amount': forms.NumberInput(attrs={'class': 'form-control'}),
            'broker': forms.Select(attrs={'class': 'form-control'}),
        }

        labels = {
            'name': 'Nome',
            'amount': 'Valor',
            'broker': 'Corretora',
        }
