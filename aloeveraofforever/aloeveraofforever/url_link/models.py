from django.db import models


class URLLinks(models.Model):
    """ url field should not be the same with urls in urls.py """
    url = models.TextField(max_length=500, null=True, blank=True, default='')
    link = models.TextField(max_length=500, null=True, blank=True, default='')

    def __unicode__(self):
        return '%s %s' % (self.url, self.link)

    class Meta:
        db_table = "url_link"
        ordering = ('url', 'link')
        verbose_name = "Object URL"
