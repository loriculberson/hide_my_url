from django.shortcuts import render
from django.http import HttpResponseRedirect

from .models import Url

def index(request):
  return render(request, 'cloak/index.html')

def new_url(request):
  encrypted_code = 'random123'
  original_url = request.POST['user_added_url']
  
  if original_url.startswith('http://'):
    original_url = original_url
  else:
    original_url = 'http://' + original_url 

  encrypted_url = original_url + '/' + encrypted_code
  final_url = Url(user_added_url = original_url, obfuscated_url = encrypted_url)
  final_url.save()

  return render(request, 'cloak/new_url.html', { 'final_url' : final_url })