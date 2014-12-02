from django.shortcuts import render
from django.template.response import TemplateResponse
from django.core.mail import EmailMessage
from django.contrib import messages
from django.conf import settings

from django.shortcuts import render_to_response, redirect
from django.template import RequestContext, loader, Context
import os
from pygeocoder import Geocoder
from configurations import settings as conf_settings
from models import *
from healthcalc.models import *
from url_link.models import URLLinks


EMAIL_DIRS = settings.EMAIL_DIRS
atp_number = conf_settings["ATP_NUMBER"]
geo_data = settings.GEO_DATA
default_country = {'country_code': 'USA', 'country_lang': 'en'}


def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip


def get_country_code(request):
    import pygeoip
    gi = pygeoip.GeoIP(geo_data)
    country_ip = get_client_ip(request)
    c_country = gi.country_name_by_addr(country_ip)
    return c_country


def get_country(request):
    country = get_country_code(request)
    flpcountries = {'Australia':'AUS', 'Belgium':'BEL', 'Canada':'CAN',
                    'Czech':'CZE', 'Greece':'GRC', 'Ireland':'IRL', 'Luxembourg':'LUX',
                    'Netherlands':'NLD', 'New Zealand':'NZL', 'Northern Ireland':'ILN',
                    'Philippines':'PHL', 'Portugal':'PRT', 'Slovakia':'SVK', 'South Africa':'ZAF',
                    'Spain':'ESP', 'United Kingdom':'GBR', 'United States':'USA',
                    'Great Britain':'GBR', 'Malaysia':'MYS', 'Singapore':'SGP', 'Mexico':'MEX'}
    flplanguage = {'Australia':'en', 'Belgium':'nl', 'Canada':'en',
                    'Czech':'cs', 'Greece':'el', 'Ireland':'en', 'Luxembourg':'de',
                    'Netherlands':'nl', 'New Zealand':'en', 'Northern Ireland':'en',
                    'Philippines':'en', 'Portugal':'pt', 'Slovakia':'sk', 'South Africa':'en',
                    'Spain':'es', 'United Kingdom':'en', 'United States':'en',
                    'Great Britain':'en', 'Malaysia':'en', 'Singapore':'en', 'Mexico':'es'}
    try:
        country_code = flpcountries[country]
        country_lang = flplanguage[country]
        current_country = "Your current country is " + country
    except:
        country_code = 'USA'
        country_lang = 'en'
    return {'country_code': country_code, 'country_lang': country_lang, 'current_country': current_country}


def getlatlong(request):

    return str(request.GET.get('longitude')), str(request.GET.get('latitude'))


def home(request):
    if request.method == 'POST':
        f = open(EMAIL_DIRS, 'a')
        f.write(request.POST['email'] + "\n")
        f.close()

    latlong = getlatlong(request)
    print latlong
    request.session["latlong"] = latlong
    
    latitude=longitude=""
    
    if latlong[0] != 'None':
        longitude, latitude = getlatlong(request)
        return render_to_response('ajax.html', dict(
                country = (latitude + ',' + longitude),
                atp_number = conf_settings["ATP_NUMBER"],
                twitter = conf_settings["Twitter"],
                email = conf_settings["Email"],
                mobile = conf_settings["Mobile"],
                linkedin = conf_settings["Linkedin"],
                facebook = conf_settings["Facebook"],
                youtube = conf_settings["Youtube"],
                name = conf_settings["NAME"],
                ), context_instance=RequestContext(request))
    else:
        return render_to_response('home.html', dict(
                country = (latitude + ',' + longitude),
                home_id="current",
                atp_number = conf_settings["ATP_NUMBER"],
                twitter = conf_settings["Twitter"],
                email = conf_settings["Email"],
                mobile = conf_settings["Mobile"],
                linkedin = conf_settings["Linkedin"],
                facebook = conf_settings["Facebook"],
                youtube = conf_settings["Youtube"],
                name = conf_settings["NAME"],
                ), context_instance=RequestContext(request))


def about(request):
    return render_to_response('about.html', dict(pages_id="current",), context_instance=RequestContext(request))


def contact(request):
    return render_to_response('contact.html', dict(pages_id="current",), context_instance=RequestContext(request))


def faqs(request):
    return render_to_response('faqs.html', dict(pages_id="current",), context_instance=RequestContext(request))


def opportunity(request):
    return render_to_response('opportunity.html', dict(pages_id="current",), context_instance=RequestContext(request))


def benefits(request):
    return render_to_response('benefits-of-aloe.html', dict(pages_id="current",), context_instance=RequestContext(request))


def products(request):
    return render_to_response('forever-living-products.html', dict(pages_id="current",), context_instance=RequestContext(request))


def uses(request):
    return render_to_response('aloe-vera-uses.html', dict(pages_id="current",), context_instance=RequestContext(request))


def stories(request):
    return render_to_response('stories.html', dict(pages_id="current",), context_instance=RequestContext(request))


def weight_loss(request):
    return render_to_response('weight-loss.html', dict(pages_id="current",), context_instance=RequestContext(request))


def drinks(request):
    country_details = get_country(request)
    country = country_details['country_code']
    lang = country_details['country_lang']
    return redirect('https://www.foreverliving.com/retail/entry/Shop.do?language='+lang+'&store='+country+'&distribID='
                    + str(atp_number)+'&categoryName=DrinksR')


def nutrition(request):
    country_details = get_country(request)
    country = country_details['country_code']
    lang = country_details['country_lang']
    return redirect('https://www.foreverliving.com/retail/entry/Shop.do?language='+lang+'&store='+country+'&distribID='
                    + str(atp_number)+'&categoryName=NutritionR')


def bee_products(request):
    country_details = get_country(request)
    country = country_details['country_code']
    lang = country_details['country_lang']
    return redirect('https://www.foreverliving.com/retail/entry/Shop.do?language='+lang+'&store='+country+'&distribID='
                    + str(atp_number)+'&categoryName=Bee_ProductsR')


def weight_management(request):
    country_details = get_country(request)
    country = country_details['country_code']
    lang = country_details['country_lang']
    return redirect('https://www.foreverliving.com/retail/entry/Shop.do?language='+lang+'&store='+country+'&distribID='
                    + str(atp_number)+'&categoryName=Weight_ManagementR')


def personal_care(request):
    country_details = get_country(request)
    country = country_details['country_code']
    lang = country_details['country_lang']
    return redirect('https://www.foreverliving.com/retail/entry/Shop.do?language='+lang+'&store='+country+'&distribID='
                    + str(atp_number)+'&categoryName=Personal_CareR')


def skin_care(request):
    country_details = get_country(request)
    country = country_details['country_code']
    lang = country_details['country_lang']
    return redirect('https://www.foreverliving.com/retail/entry/Shop.do?language='+lang+'&store='+country+'&distribID='
                    + str(atp_number)+'&categoryName=Skin_CareR')


def business_packs(request):
    country_details = get_country(request)
    country = country_details['country_code']
    lang = country_details['country_lang']
    return redirect('https://www.foreverliving.com/retail/entry/Shop.do?language='+lang+'&store='+country+'&distribID='
                    + str(atp_number)+'&categoryName=Business_PacksR')


def combo_packs(request):
    country_details = get_country(request)
    country = country_details['country_code']
    lang = country_details['country_lang']
    return redirect('https://www.foreverliving.com/retail/entry/Shop.do?language='+lang+'&store='+country+'&distribID='
                    + str(atp_number)+'&categoryName=Combo_PacksR')


def sonya_skin_care(request):
    country_details = get_country(request)
    country = country_details['country_code']
    lang = country_details['country_lang']
    return redirect('https://www.foreverliving.com/retail/entry/Shop.do?language='+lang+'&store='+country+'&distribID='
                    + str(atp_number)+'&categoryName=Sonya_Skin_CareR')


def sonya_cosmetics(request):
    country_details = get_country(request)
    country = country_details['country_code']
    lang = country_details['country_lang']
    return redirect('https://www.foreverliving.com/retail/entry/Shop.do?language='+lang+'&store='+country+'&distribID='
                    + str(atp_number)+'&categoryName=DrinksR')


def literature(request):
    country_details = get_country(request)
    country = country_details['country_code']
    lang = country_details['country_lang']
    return redirect('https://www.foreverliving.com/retail/entry/Shop.do?language='+lang+'&store='+country+'&distribID='
                    + str(atp_number)+'&categoryName=LiteraturesR')


def shop(request):
    country_details = get_country(request)
    country = country_details['country_code']
    lang = country_details['country_lang']
    return redirect('https://www.foreverliving.com/retail/entry/Shop.do?language='+lang+'&store='+country+'&distribID='
                    + str(atp_number))


def aloe_vera_gel(request):
    country_details = get_country(request)
    country = country_details['country_code']
    lang = country_details['country_lang']
    return redirect('https://www.foreverliving.com/marketing/Product.do?code=015&language='+lang+'&store='+country+'&distribID='
                    + str(atp_number))


def forever_daily(request):
    country_details = get_country(request)
    country = country_details['country_code']
    lang = country_details['country_lang']
    return redirect('https://www.foreverliving.com/marketing/Product.do?code=439&language='+lang+'&store='+country+'&distribID='
                    + str(atp_number))


def fabx(request):
    country_details = get_country(request)
    country = country_details['country_code']
    lang = country_details['country_lang']
    return redirect('https://www.foreverliving.com/marketing/Product.do?code=440&language='+lang+'&store='+country+'&distribID='
                    + str(atp_number))


def vital5(request):
    country_details = get_country(request)
    country = country_details['country_code']
    lang = country_details['country_lang']
    return redirect('https://www.foreverliving.com/marketing/Product.do?code=456&language='+lang+'&store='+country+'&distribID='
                    + str(atp_number))


def join(request):
    country_details = get_country(request)
    country= country_details['country_code']
    lang = country_details['country_lang']
    return redirect('https://www.foreverliving.com/marketing/joinnow/applicationForm.do?action=display'
                    '&store='+country+'&langID='+lang+'&distribID='+ str(atp_number))


def get_products_url(request, url=None):
    return render_to_response('urls.html', dict(pages_id="current", urls=ProductsURLs.objects.all()),
                              context_instance=RequestContext(request))


def urls_links(request, urls=None):
    """This is a dynamic views for a dynamic url """
    country_details = get_country(request)
    country = country_details['country_code']
    lang = country_details['country_lang']
    link = {}
    urls_and_links = URLLinks.objects.filter(url=urls)
    for url_link in urls_and_links:
        item = str(url_link).split(' ')
        link['url'] = str(item[0])
        link['link'] = str(item[1])
    if urls == link['url']:
        return redirect(link['link'] + '&language='+lang+'&store='+country+'&distribID='+ str(atp_number))