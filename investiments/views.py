from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from . import models, forms


class InvestimentListView(ListView):
    model = models.Investiment
    template_name = 'investiment_list.html'
    context_object_name = 'investiments'

    def get_queryset(self):
        queryset = super().get_queryset()
        name = self.request.GET.get('name')

        if name:
            queryset = queryset.filter(name__icontains=name)

        return queryset


class InvestimentCreateView(CreateView):
    model = models.Investiment
    template_name = 'investiment_create.html'
    form_class = forms.InvestimentForm
    success_url = reverse_lazy('investiment_list')


class InvestimentUpdateView(UpdateView):
    model = models.Investiment
    template_name = 'investiment_update.html'
    form_class = forms.InvestimentForm
    success_url = reverse_lazy('investiment_list')


class InvestimentDeleteView(DeleteView):
    model = models.Investiment
    template_name = 'investiment_delete.html'
    success_url = reverse_lazy('investiment_list')
