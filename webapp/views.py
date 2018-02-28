from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from webapp.models import Webapp, Shikigami
from django.shortcuts import get_object_or_404, redirect, render
import os

# Create your views here.



# ======================Data=============================

class IndexView(ListView):
    template_name = 'webapp/index.html'
    context_object_name = 'item'
    print "Go to Index Page"
    def get_queryset(self):
        return Webapp.objects.all()

class ShikigamiDetailView(ListView):
    template_name = "webapp/shikigami_page.html"
    context_object_name = "shikigami_list"

    def get_queryset(self):
        return Shikigami.objects.all()
    #
    # def get(self, request, *args, **kwargs):
    #     return render(request, self.template_name, {})

