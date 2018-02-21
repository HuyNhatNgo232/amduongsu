from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from webapp.models import Webapp

# Create your views here.

class IndexView(ListView):
    template_name = 'webapp/index.html'
    context_object_name = 'index'

    def get_queryset(self):
        return Webapp.objects.all()