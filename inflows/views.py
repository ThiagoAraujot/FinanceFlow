from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from . import models, forms


class InflowListView(ListView):
    model = models.Inflow
    template_name = 'inflow_list.html'
    context_object_name = 'inflows'

    def get_queryset(self):
        queryset = super().get_queryset()
        title = self.request.GET.get('title')

        if title:
            queryset = queryset.filter(title__icontains=title)

        return queryset


class InflowCreateView(CreateView):
    model = models.Inflow
    template_name = 'inflow_create.html'
    form_class = forms.InflowForm
    success_url = reverse_lazy('inflow_list')


class InflowUpdateView(UpdateView):
    model = models.Inflow
    template_name = 'inflow_update.html'
    form_class = forms.InflowForm
    success_url = reverse_lazy('inflow_list')


class InflowDeleteView(DeleteView):
    model = models.Inflow
    template_name = 'inflow_delete.html'
    success_url = reverse_lazy('inflow_list')
