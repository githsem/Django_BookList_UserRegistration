from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView
from django.urls import reverse_lazy

from .models import Book

# Create your views here.

class BookList(ListView):
    model = Book
    context_object_name = 'books'

class BookDetail(DetailView):
    model = Book   
    context_object_name = 'book' 

class BookCreate(CreateView):
    model = Book   
    fields = '__all__'  
    success_url = reverse_lazy('books')

class BookUpdate(UpdateView):
    model = Book 
    fields = '__all__'  
    success_url = reverse_lazy('books')   
    
    

