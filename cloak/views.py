from django.shortcuts import render, redirect
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
    code = get_random_string(length=11)

    final_url = Url(user_added_url = original_url, obfuscated_key = code)
    final_url.save()
  
  urls = Url.objects.order_by('-id')
  return render(request, 'cloak/new_url.html', { 'final_url' : final_url, 'urls' : urls })

def hit_counter(request, code):
  url = Url.objects.get(obfuscated_key = code)
  url.obfuscated_url_click_counter +=1
  url.save()
  return redirect(url.user_added_url)



