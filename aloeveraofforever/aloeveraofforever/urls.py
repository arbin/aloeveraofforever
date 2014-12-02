from django.conf.urls import patterns, include, url
#from django.views.generic import TemplateView
from django.conf.urls.static import static
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

from django.contrib.sitemaps import GenericSitemap
from sitemap import *
from flp.models import ProductsURLs
from url_link.models import URLLinks
from datetime import datetime

from settings import local

#sitemaps = {'products': ProductsSitemap, 'apps': AppsSitemap}
sitemaps = {'products': ProductsSitemap}

blog_urls = [
    url(r'^', include('zinnia.urls.capabilities')),
    url(r'^search/', include('zinnia.urls.search')),
    url(r'^sitemap/', include('zinnia.urls.sitemap')),
    url(r'^trackback/', include('zinnia.urls.trackback')),
    url(r'^blog/tags/', include('zinnia.urls.tags')),
    url(r'^blog/feeds/', include('zinnia.urls.feeds')),
    url(r'^blog/random/', include('zinnia.urls.random')),
    url(r'^blog/authors/', include('zinnia.urls.authors')),
    url(r'^blog/categories/', include('zinnia.urls.categories')),
    url(r'^blog/comments/', include('zinnia.urls.comments')),
    url(r'^blog/', include('zinnia.urls.entries')),
    url(r'^blog/', include('zinnia.urls.archives')),
    url(r'^blog/', include('zinnia.urls.shortlink')),
    url(r'^blog/', include('zinnia.urls.quick_entry'))
]

""" This produces a dynamic url added to urlpatterns """
prod_urls = []
urls_and_links = URLLinks.objects.all()
for url_link in urls_and_links:
    urls = str(url_link).split(' ')
    prod_urls.append(url(urls[0]+"/", 'flp.views.urls_links', {'urls': urls[0]}, name=urls[0]))


urlpatterns = patterns('',
    #url(r'^$', TemplateView.as_view(template_name='base.html')),
    # Examples:
    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    (r'^grappelli/', include('grappelli.urls')), # grappelli URLS
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'flp.views.home', name='home'),
    #url(r'^blog', include('cms.urls')),
    #pages
    url(r'^about', 'flp.views.about', name='about'),
    url(r'^faqs', 'flp.views.faqs', name='faqs'),
    url(r'^opportunity', 'flp.views.opportunity', name='opportunity'),
    url(r'^benefits-of-aloe', 'flp.views.benefits', name='benefits'),
    url(r'^forever-living-products', 'flp.views.products', name='products'),
    url(r'^aloe-vera-uses', 'flp.views.uses', name='uses'),
    url(r'^stories', 'flp.views.stories', name='stories'),
    url(r'^contact', 'flp.views.contact', name='contact'),
    #apps
    url(r'^body-mass-index', 'healthcalc.views.bmi', name='body-mass-index'),
    url(r'^calorie-burned-for-running', 'healthcalc.views.calorie_burn', name='calorie_burn'),
    url(r'^basal-metabolic-rate', 'healthcalc.views.bmr', name='bmr'),
    url(r'^how-many-calories-will-i-burn', 'healthcalc.views.calories', name='calories'),
    url(r'^weight-loss', 'flp.views.weight_loss', name='weight-loss'),
    url(r'^calorie-counter', 'healthcalc.views.calorie_counter', name='calorie-counter'),
    url(r'^cost-of-smoking', 'healthcalc.views.cost_of_smoking', name='cost-of-smoking'),
    url(r'^pregnancy-gestational-diabetes-diet-calculator', 'healthcalc.views.pregnancy_diabetes', name='pregnancy-diabetes'),
    url(r'^ww-food-points', 'healthcalc.views.ww_food_points', name='ww-food-points'),
    #products
    url(r'^drinks', 'flp.views.drinks', name='drinks'),
    url(r'^nutrition', 'flp.views.nutrition', name='nutrition'),
    url(r'^bee_products', 'flp.views.bee_products', name='bee_products'),
    url(r'^weight_management', 'flp.views.weight_management', name='weight_management'),
    url(r'^personal_care', 'flp.views.personal_care', name='personal_care'),
    url(r'^skin_care', 'flp.views.skin_care', name='skin_care'),
    url(r'^combo_packs', 'flp.views.combo_packs', name='combo_packs'),
    url(r'^business_packs', 'flp.views.business_packs', name='business_packs'),
    url(r'^sonya_skin_care', 'flp.views.sonya_skin_care', name='sonya_skin_care'),
    url(r'^sonya_cosmetics', 'flp.views.sonya_cosmetics', name='sonya_cosmetics'),
    url(r'^literature', 'flp.views.literature', name='literature'),
    url(r'^shop', 'flp.views.shop', name='shop'),
    url(r'^aloe_vera_gel', 'flp.views.aloe_vera_gel', name='aloe_vera_gel'),
    url(r'^forever_daily', 'flp.views.forever_daily', name='forever_daily'),
    url(r'^fabx', 'flp.views.fabx', name='fabx'),
    url(r'^vital5', 'flp.views.vital5', name='vital5'),
    url(r'^join', 'flp.views.join', name='join'),
    #blog
    url(r'^weblog/', include('zinnia.urls', namespace='zinnia')),
    url(r'^comments/', include('django_comments.urls')),
    url(r'^', include(blog_urls, namespace='zinnia')),
    url(r'^', include(prod_urls, namespace='urls_links')),
    #sitemap
    url(r'^(?P<url>.*)/', 'flp.views.get_products_url', name='url_products'),
    #url(r'^(?P<url>.*)/', 'flp.views.get_apps_url', name='url_apps'),
    url(r'^sitemap.xml$', 'django.contrib.sitemaps.views.sitemap', {'sitemaps': sitemaps}),
    #products urls
    #url(r'^products_url', 'flp.views.get_products_url', name='products_url'),
)