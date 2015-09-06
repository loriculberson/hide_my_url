from django.contrib import admin

from .models import Url

class UrlAdmin(admin.ModelAdmin):
  list_display = ('user_added_url','obfuscated_url')

admin.site.register(Url, UrlAdmin)
# Register your models here.
