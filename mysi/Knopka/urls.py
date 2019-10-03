from django.urls import path, include
from django.views.generic import ListView, DetailView
from Knopka.models import opa
from .views import *

app_name = "knopka"

urlpatterns = [
    path("", KnopkaListView.as_view(),name = "index"),
    path("<int:pk>", KnopkaDetailView.as_view(), name = "detail"),
]
