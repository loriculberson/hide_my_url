from django.db import models
from django.utils import timezone

class Url(models.Model):
  user_added_url = models.URLField(max_length=200)
  obfuscated_url = models.URLField(max_length=200)
  obfuscated_url_click_counter = models.IntegerField(default=0)

  def __str__(self):
    return self.user_added_url

  def __str__(self):
    return self.obfuscated_url
