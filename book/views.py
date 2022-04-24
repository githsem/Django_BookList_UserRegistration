from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Book

# Create your views here.

class CustomLoginView(LoginView):
    template_name = 'book/login.html'
    fields = '__all__'
    redirect_authenticated_user = True
    
    def get_success_url(self):
        return reverse_lazy('books')

class BookList(LoginRequiredMixin, ListView):
    model = Book
    context_object_name = 'books'

class BookDetail(LoginRequiredMixin, DetailView):
    model = Book   
    context_object_name = 'book' 

class BookCreate(LoginRequiredMixin, CreateView):
    model = Book   
    fields = '__all__'  
    success_url = reverse_lazy('books')

class BookUpdate(LoginRequiredMixin, UpdateView):
    model = Book 
    fields = '__all__'  
    success_url = reverse_lazy('books') 

class BookDelete(LoginRequiredMixin, DeleteView):
    model = Book
    context_object_name = 'book'
    success_url = reverse_lazy('books') 
    

