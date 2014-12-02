from django.contrib import sitemaps
from django.contrib.sitemaps import Sitemap
from django.core.urlresolvers import reverse

from datetime import datetime

from flp.models import *
from healthcalc.models import *


class ProductsSitemap(Sitemap):
    priority = 0.5

    def items(self):
        return ProductsURLs.objects.all()

    def changefreq(self, obj):
        return 'weekly'

    #def lastmod(self, obj):
    #    return datetime.now()


class AppsSitemap(Sitemap):
    priority = 0.5

    def items(self):
        return AppsURLs.objects.all()

    def changefreq(self, obj):
        return 'weekly'

    #def lastmod(self, obj):
    #    return datetime.now()

