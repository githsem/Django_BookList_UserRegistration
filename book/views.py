from django.shortcuts import render, redirect
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from .models import Book

# Create your views here.

class CustomLoginView(LoginView):
    template_name = 'book/login.html'
    fields = '__all__'
    redirect_authenticated_user = True
    
    def get_success_url(self):
        return reverse_lazy('books')

class RegisterPage(FormView):
    template_name = 'book/register.html'
    form_class = UserCreationForm
    redirect_authenticated_user = True
    success_url = reverse_lazy('books')   

    def form_valid(self, form):
        user = form.save()
        if user is not None:
            login(self.request, user)   
        return super(RegisterPage,self).form_valid(form)      

    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('books')
        return super(RegisterPage,self).get(*args, **kwargs)   

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
    fields = ['title', 'author', 'isbn', 'isread']   
    success_url = reverse_lazy('books')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(BookCreate, self).form_valid(form)

class BookUpdate(LoginRequiredMixin, UpdateView):
    model = Book 
    fields = ['title', 'author', 'isbn', 'isread']  
    success_url = reverse_lazy('books') 

class BookDelete(LoginRequiredMixin, DeleteView):
    model = Book
    context_object_name = 'book'
    success_url = reverse_lazy('books') 
    

