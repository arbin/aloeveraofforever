from django.contrib import admin
from configurations.models import Configuration


class ConfigurationAdmin(admin.ModelAdmin):
    list_display = ('name', 'value')
    
admin.site.register(Configuration, ConfigurationAdmin)
