from django.contrib import admin

# Register your models here.
from models import *


class AppsURLsAdmin(admin.ModelAdmin):
    list_display = ('url',)
    search_fields = ('url',)
admin.site.register(AppsURLs, AppsURLsAdmin)