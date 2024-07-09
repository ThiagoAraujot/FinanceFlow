from django.utils.formats import number_format
from outflows.models import Outflows
from inflows.models import Inflow
from investiments.models import Investiment


def get_metrics():
    inflows = Inflow.objects.all()
    outflows = Outflows.objects.all()
    investiments = Investiment.objects.all()

    total_outflows = sum(outflow.amount for outflow in outflows)
    total_inflows = sum(inflow.amount for inflow in inflows)
    total_profit = total_inflows - total_outflows
    total_investiments = sum(
        investiment.amount for investiment in investiments)

    return dict(
        total_outflows=number_format(
            total_outflows, decimal_pos=2, force_grouping=True),
        total_inflows=number_format(
            total_inflows, decimal_pos=2, force_grouping=True),
        total_profit=total_profit,
        total_investiments=number_format(
            total_investiments, decimal_pos=2, force_grouping=True)
    )
