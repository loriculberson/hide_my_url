from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.utils.crypto import get_random_string

from .models import Url

def index(request):
  return render(request, 'cloak/index.html')

def new_url(request):
  user_input = request.POST['user_added_url']

  if user_input.startswith('http://'):
    original_url = user_input
  else:
    original_url = 'http://' + user_input

  try:
    final_url = Url.objects.get(user_added_url = original_url)
  except Url.DoesNotExist:
    encrypted_code = get_random_string(length=11)
    encrypted_url = original_url + '/' + encrypted_code

    final_url = Url(user_added_url = original_url, obfuscated_url = encrypted_url)
    final_url.save()
  
  urls = Url.objects.order_by('-id')
  return render(request, 'cloak/new_url.html', { 'final_url' : final_url, 'urls' : urls })