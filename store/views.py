from store.models import Category, Product

from django.shortcuts import render
from django.views.generic import ListView, DetailView

# Create your views here.

class HomeListView(ListView):
	model = Product
	template_name = 'store/index.html'
	context_object_name = 'products'