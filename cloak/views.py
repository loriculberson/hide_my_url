from django.shortcuts import render
from django.http import HttpResponseRedirect

from .models import Url

def index(request):
  return render(request, 'cloak/index.html')

def new_url(request):
  return render(request, 'cloak/new_url.html')