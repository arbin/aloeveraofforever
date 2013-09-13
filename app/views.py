from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.template.response import TemplateResponse

import json

from socialregistration.contrib.facebook.models import FacebookProfile


from django.conf import settings
from django.http import HttpResponse

#from app.models import AlternativeMedicine

MEDIA_ROOT = settings.MEDIA_ROOT
APIkey = "AIzaSyDB8YB1Ww_VC5j52_QQTzDityPXKCfHRy8"
lat = 9.295552
lng = 123.281494

class Facebook(object):
    def __init__(self, user=None):
        if user is None:
            self.uid = None
        else:
            self.uid = user['uid']
            self.user = user
            self.graph = facebook.GraphAPI(user['access_token'])

def index(request):
    #featured_list = AlternativeMedicine.objects.all()

    if request.user.is_authenticated():
        return render_to_response(
            'main.html', dict(
                facebook=FacebookProfile.objects.all(),
        ), context_instance=RequestContext(request))
    else:
        return render_to_response(
            'home.html', dict(
                facebook=FacebookProfile.objects.all(),               
                #listfeatured=featured_list,
        ), context_instance=RequestContext(request))


"""
def add_remedies(request):
    user = "3"
    existingcollections = Collections.objects.filter(owner=user)

    if request.method == "POST":
        if request.POST.get('existingcollection', None) == "":
            collname = request.POST.get('collectionname', None)
        else:
            collname = request.POST.get('existingcollection', None)

        try:
            entry = AlternativeMedicine(name=request.POST.get('name', None),
                            scientific_name=request.POST.get('scientificname', None),
                            description=request.POST.get('caption', None),
                            remedies_for=request.POST.get('healthtopic', None),
                            where_source=request.POST.get('source', None),
                            way_to_use=request.POST.get('ways', None),
                            related_website=request.POST.get('link', None),
                            image=request.POST.get('image', None),
                            collection_name=collname,
                            )
            entry.save()
            FILE_UPLOAD_DIR = MEDIA_ROOT + 'img/image/'
            filename = request.FILES['image'].name
            destination = open(FILE_UPLOAD_DIR + filename, 'wb+')
            for chunk in request.FILES['image'].chunks():
                destination.write(chunk)
            destination.close()
            whereto = WhereToBuy(id=entry.id, lat=request.POST.get('lat', None), lng=request.POST.get('lng', None))
            whereto.save()
        except ValueError:
            msg = "Error"

    #return TemplateResponse(request, 'add-remedies.html', None)
    return render_to_response(
            'add-remedies.html', dict(
                existingcollections=existingcollections), context_instance=RequestContext(request))
"""
