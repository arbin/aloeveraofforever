from django.db import models

# Create your models here.


class ProductsURLs(models.Model):
    url = models.TextField(max_length=500, null=True, blank=True, default='')

    def __unicode__(self):
        return self.url

    @models.permalink
    def get_absolute_url(self):
        return ('url_products', (self.url,))


    class Meta:
        db_table = "flp_products_url"
        ordering = ('url',)
        verbose_name = "Products URL"