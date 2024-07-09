from django import forms
from . import models


class OutflowForm(forms.ModelForm):

    class Meta:
        model = models.Outflows
        fields = ['title', 'amount', 'category', 'description',]

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'amount': forms.NumberInput(attrs={'class': 'form-control'}),
            'category': forms.Select(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 3})
        }

        labels = {
            'title': 'Nome',
            'amount': 'Valor',
            'category': 'Categoria',
            'description': 'Descrição',
        }
