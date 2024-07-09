from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', include('brokers.urls')),
    path('', include('categories.urls')),
    path('', include('investiments.urls')),
    path('', include('outflows.urls')),
]
