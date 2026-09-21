from django.urls import path
from .views import get_catalog

urlpatterns = [
    path('', get_catalog),
]