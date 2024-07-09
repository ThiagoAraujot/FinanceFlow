from django.urls import path
from . import views

urlpatterns = [
    path('investiments/list/', views.InvestimentListView.as_view(),
         name="investiment_list"),
    path('investiments/create/', views.InvestimentCreateView.as_view(),
         name="investiment_create"),
    path('investiments/<int:pk>/update/',
         views.InvestimentUpdateView.as_view(), name="investiment_update"),
    path('investiments/<int:pk>/delete/',
         views.InvestimentDeleteView.as_view(), name="investiment_delete"),
]
