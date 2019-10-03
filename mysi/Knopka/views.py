from django.shortcuts import render
from django.views.generic import ListView, DetailView

from .models import opa
# Create your views here.

class KnopkaListView(ListView):
    model = opa
    queryset=opa.objects.all().order_by("-date")[:10]


class KnopkaDetailView(DetailView):
    model = opa
