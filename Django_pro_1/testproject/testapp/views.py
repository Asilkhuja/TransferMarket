from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse('Hello, World!<br>'
                        '<a href="/about">About</a><br>'
                        '<a href="/contacts">Contacts</a>')

def about(request):
    return HttpResponse('This is my first site<br>'
                        '<a href = "/">home</a<br>')

def contacts(request):
    return HttpResponse('Our contacts:<br> '
                        'Telefon: +9999999999 👍<br>'
                        'E-mail:<br>'
                        '<a href = "/">home</a')