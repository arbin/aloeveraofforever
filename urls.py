from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

from aloeveraofforever import settings

urlpatterns = patterns('',
    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    #url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'aloeveraofforever.views.home', name='home'),
    url(r'^about', 'aloeveraofforever.views.about', name='about'),
    url(r'^faqs', 'aloeveraofforever.views.faqs', name='faqs'),
    url(r'^opportunity', 'aloeveraofforever.views.opportunity', name='opportunity'),
    url(r'^benefits-of-aloe', 'aloeveraofforever.views.benefits', name='benefits'),
    url(r'^forever-living-products', 'aloeveraofforever.views.products', name='products'),
    url(r'^aloe-vera-uses', 'aloeveraofforever.views.uses', name='uses'),
    url(r'^stories', 'aloeveraofforever.views.stories', name='stories'),
    url(r'^body-mass-index', 'aloeveraofforever.views.bmi', name='bmi'),
    url(r'^calorie-burned-for-running', 'aloeveraofforever.views.calorie_burn', name='calorie_burn'),
    url(r'^basal-metabolic-rate', 'aloeveraofforever.views.bmr', name='bmr'),
    url(r'^how-many-calories-will-i-burn', 'aloeveraofforever.views.calories', name='calories'),
    url(r'^weight-loss', 'aloeveraofforever.views.weight_loss', name='weight-loss'),
    url(r'^calorie-counter', 'aloeveraofforever.views.calorie_counter', name='calorie_counter'),
    url(r'^cost-of-smoking', 'aloeveraofforever.views.cost_of_smoking', name='cost-of-smoking'),
    url(r'^pregnancy-gestational-diabetes-diet-calculator', 'aloeveraofforever.views.pregnancy_diabetes', name='pregnancy-diabetes'),
    url(r'^ww-food-points', 'aloeveraofforever.views.ww_food_points', name='ww-food-points'),
)

if settings.DEBUG:
    urlpatterns += patterns('',
        (r'^media/(?P<path>.*)$', 'django.views.static.serve',
        {'document_root': settings.MEDIA_ROOT}),
    )