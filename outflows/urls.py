from django.urls import path
from . import views

urlpatterns = [
    path('outflows/list/', views.OutflowListView.as_view(),
         name="outflow_list"),
    path('outflows/create/', views.OutflowCreateView.as_view(),
         name="outflow_create"),
    path('outflows/<int:pk>/update/',
         views.OutflowUpdateView.as_view(), name="outflow_update"),
    path('outflows/<int:pk>/delete/',
         views.OutflowDeleteView.as_view(), name="outflow_delete"),
]
