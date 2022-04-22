from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .models import Book

# Create your views here.

class BookList(ListView):
    model = Book
    context_object_name = 'books'

class BookDetail(DetailView):
    model = Book   
    context_object_name = 'book' 
    
    

