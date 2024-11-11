from django.contrib import admin
from .models import Config

class ConfigAdmin(admin.ModelAdmin):
    list_display = ('Nome','url','typeauth')

admin.site.register(Config, ConfigAdmin)