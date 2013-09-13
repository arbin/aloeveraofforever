import json
import httplib
import lxml.html
import socket
import urllib2
import urlparse

import PIL
from PIL import Image

from urllib2 import URLError, HTTPError

from django.core.validators import URLValidator
from django.core.exceptions import ValidationError

socket.setdefaulttimeout(10)

def get_url_content(url):
    try:
        f = urllib2.urlopen(url)
        content = f.read()
        return content
    except HTTPError:
        return 0
    except URLError:
        return 0
    except ValueError:
        return 0

    return 0

def check_content_type(url):
    #try:
        o=urlparse.urlparse(url)

        conn = httplib.HTTPConnection(o.netloc)
        conn.request("HEAD", o.path)
        res = conn.getresponse()

        content_type = res.getheader('content-type')
        if content_type.startswith('image'):
            return 'image'
        else:
            return 'text'
    #except:
        return 'text'

def validate_url(url):
    valid_url = URLValidator(verify_exists=False)

    try:
        valid_url(url)
    except ValidationError:
        return 0

    return 1

def get_images(url):
    if validate_url(url):
        images = []
        if check_content_type(url) == 'image':
            images.append(url)
        else:
            content = get_url_content(url)
            if content == 0:
                return 0
            tree = lxml.html.fromstring(content)

            for image in tree.xpath("//img/@src"):
                if not image.startswith('http://'):
                    image = urlparse.urljoin(url, image)

                if image not in images:
                    images.append(image)

        return images
    return 0


def resize(image, image_out, basewidth=192):
    basewidth = basewidth
    img = Image.open(image)
    wpercent = (basewidth/float(img.size[0]))
    hsize = int((float(img.size[1])*float(wpercent)))
    img = img.resize((basewidth,hsize), PIL.Image.ANTIALIAS)
    img.save(image_out , quality=90)



@csrf_exempt
def upload(request):
    if request.method == "POST":
        if request.is_ajax( ):
            upload = request
            is_raw = True
            try:
                filename = request.GET[ 'qqfile' ]
            except KeyError:
                return HttpResponseBadRequest( "AJAX request not valid" )
        else:
            is_raw = False
            if len( request.FILES ) == 1:
                upload = request.FILES.values( )[ 0 ]
            else:
                raise Http404( "Bad Upload" )
            filename = upload.name

        #str = "%f" % time.time()
        #str = str.replace('.', '')

        #filename = "%s%s" % (str, os.path.splitext(filename)[1])
        filename = create_filename(filename)

        # save the file
        success = save_upload( upload, filename, is_raw )

        if success:
            image_o = "%s/pin/temp/o/%s" % (MEDIA_ROOT, filename)
            image_t = "%s/pin/temp/t/%s" % (MEDIA_ROOT, filename)

            resize(image_o, image_t, 99)

        ret_json = {'success':success,'file':filename}
        return HttpResponse( json.dumps( ret_json ) )

def a_sendurl(request):
    if request.method == "POST":
        url = request.POST['url']

        if url == '':
            return HttpResponse(0)

        images = get_images(url)
        if images == 0:
            return HttpResponse(0)

        return HttpResponse(json.dumps(images))
    else:
        return HttpResponse(0)