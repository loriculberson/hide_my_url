from django.shortcuts import render

from .models import Url

def index(request):
  return render(request, 'cloak/index.html')

