from django.db import models


TYPES = (
    ('Renda', 'Renda'),
    ('Gasto', 'Gasto')
)


class Category(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    type = models.CharField(max_length=100, choices=TYPES)
    stipulated_maximum = models.DecimalField(
        max_digits=10, decimal_places=2, blank=True, null=True)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name
