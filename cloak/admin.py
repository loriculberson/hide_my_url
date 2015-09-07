from django.contrib import admin

from .models import Url

class UrlAdmin(admin.ModelAdmin):
  list_display = ('user_added_url','obfuscated_url', 'obfuscated_url_click_counter')

admin.site.register(Url, UrlAdmin)
