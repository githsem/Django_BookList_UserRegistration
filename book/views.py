from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def booklist(request):
    return HttpResponse('Book List')
