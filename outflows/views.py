from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from . import models, forms


class OutflowListView(ListView):
    model = models.Outflows
    template_name = 'outflow_list.html'
    context_object_name = 'outflows'

    def get_queryset(self):
        queryset = super().get_queryset()
        title = self.request.GET.get('title')

        if title:
            queryset = queryset.filter(title__icontains=title)

        return queryset


class OutflowCreateView(CreateView):
    model = models.Outflows
    template_name = 'outflow_create.html'
    form_class = forms.OutflowForm
    success_url = reverse_lazy('outflow_list')


class OutflowUpdateView(UpdateView):
    model = models.Outflows
    template_name = 'outflow_update.html'
    form_class = forms.OutflowForm
    success_url = reverse_lazy('outflow_list')


class OutflowDeleteView(DeleteView):
    model = models.Outflows
    template_name = 'outflow_delete.html'
    success_url = reverse_lazy('outflow_list')
