from django.shortcuts import render
from . import forms
from .models import Sport_new
from django.http import HttpResponse

def index(request):
    search_bar = forms.SearchForm()
    category_info = Sport_new.objects.all()

    context = {
            'form': search_bar,
            'category': category_info
    }
    return render(request, 'main/index.html', context)

def about(request):
    return render(request, 'main/about.html')