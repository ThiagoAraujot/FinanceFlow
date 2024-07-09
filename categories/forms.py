from django import forms
from . import models


class CategoryForm(forms.ModelForm):

    class Meta:
        model = models.Category
        fields = ['name', 'description', 'type', 'stipulated_maximum',]

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'type': forms.Select(attrs={'class': 'form-control'}),
            'stipulated_maximum': forms.NumberInput(attrs={'class': 'form-control'})
        }

        labels = {
            'name': 'Nome',
            'description': 'Descrição',
            'type': 'Renda / Gasto ',
            'stipulated_maximum': 'Máximo Estipulado'
        }
