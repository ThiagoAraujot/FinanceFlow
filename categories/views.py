from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from . import models, forms


class CategoryListView(ListView):
    model = models.Category
    template_name = 'category_list.html'
    context_object_name = 'categories'

    def get_queryset(self):
        queryset = super().get_queryset()
        name = self.request.GET.get('name')

        if name:
            queryset = queryset.filter(name__icontains=name)

        return queryset


class CategoryCreateView(CreateView):
    model = models.Category
    template_name = 'category_create.html'
    form_class = forms.CategoryForm
    success_url = reverse_lazy('category_list')


class CategoryUpdateView(UpdateView):
    model = models.Category
    template_name = 'category_update.html'
    form_class = forms.CategoryForm
    success_url = reverse_lazy('category_list')


class CategoryDeleteView(DeleteView):
    model = models.Category
    template_name = 'category_delete.html'
    success_url = reverse_lazy('category_list')
