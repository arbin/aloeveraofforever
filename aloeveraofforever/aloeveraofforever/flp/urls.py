from django.conf.urls import patterns, include, url
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('', url(r'^drinks', 'flp.views.drinks', name='drinks'))

