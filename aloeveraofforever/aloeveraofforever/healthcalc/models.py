from django.db import models

# Create your models here.


class AppsURLs(models.Model):
    url = models.TextField(max_length=500, null=True, blank=True, default='')

    def __unicode__(self):
        return self.url

    @models.permalink
    def get_absolute_url(self):
        return ('apps_url', (self.url,))

    class Meta:
        db_table = "health_calc_url"
        ordering = ('url',)
        verbose_name = "Apps URL"