from django.shortcuts import render
from django.views import generic, View
from django.http import HttpResponse


# Create your views here.


def index(request):
    return render(request, 'index.html')