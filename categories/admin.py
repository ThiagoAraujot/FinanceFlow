from django.contrib import admin
from . import models


class CategoryAdmin(admin.ModelAdmin):

    list_display = ['name', 'description', 'type']
    search_fields = ['name', 'type',]


admin.site.register(models.Category, CategoryAdmin)
