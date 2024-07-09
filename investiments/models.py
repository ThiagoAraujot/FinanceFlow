from django.db import models
from brokers.models import Broker


class Investiment(models.Model):
    name = models.CharField(max_length=300)
    amount = models.DecimalField(max_digits=20, decimal_places=2)
    broker = models.ForeignKey(
        Broker, on_delete=models.CASCADE, related_name='investiments')
    created_at = models.DateField(auto_now_add=True)

    class Meta:
        ordering = ['amount']

    def __str__(self):
        return self.name
