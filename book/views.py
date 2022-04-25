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

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['books']=context['books'].filter(user=self.request.user)
        return context

class BookDetail(LoginRequiredMixin, DetailView):
    model = Book   
    context_object_name = 'book' 

class BookCreate(LoginRequiredMixin, CreateView):
    model = Book   
    fields = '__all__'  
    success_url = reverse_lazy('books')

    def form_valid(self, form):
        form.istance.user = self.request.user
        return super(BookCreate, self).form_valid(form)

class BookUpdate(LoginRequiredMixin, UpdateView):
    model = Book 
    fields = ['title', 'author', 'isbn', 'isread']  
    success_url = reverse_lazy('books') 

class BookDelete(LoginRequiredMixin, DeleteView):
    model = Book
    context_object_name = 'book'
    success_url = reverse_lazy('books') 
    

