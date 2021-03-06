from django.contrib import admin

from models import *

from dbtemplates.admin import TemplateAdmin, TemplateAdminForm
from dbtemplates.models import Template

from django_ace import AceWidget

class ProxyTemplateAdminForm(TemplateAdminForm):
    def __init__(self, *args, **kwargs):
        super(ProxyTemplateAdminForm, self).__init__(*args, **kwargs)
        self.fields['content'].widget = AceWidget(mode='html', theme='monokai', width="1000px", height="500px")

class MyTemplateAdmin(TemplateAdmin):
    form = ProxyTemplateAdminForm
admin.site.unregister(Template)
admin.site.register(Template, MyTemplateAdmin)

class URLLinksAdmin(admin.ModelAdmin):
    list_display = ('url', 'link',)
    search_fields = ('url',)
admin.site.register(URLLinks, URLLinksAdmin)
