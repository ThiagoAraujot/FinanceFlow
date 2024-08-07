from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.Home.as_view(), name="home"),
    path('', include('brokers.urls')),
    path('', include('categories.urls')),
    path('', include('investiments.urls')),
    path('', include('outflows.urls')),
    path('', include('inflows.urls')),
]
