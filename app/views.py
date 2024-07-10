from typing import Any
from django.views.generic import TemplateView
from inflows.models import Inflow
from outflows.models import Outflows
from investiments.models import Investiment
from .metrics import get_metrics


class Home(TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['inflows'] = Inflow.objects.all()
        context['outflows'] = Outflows.objects.all()
        context['investiments'] = Investiment.objects.all()
        context['metrics'] = get_metrics()

        return context
