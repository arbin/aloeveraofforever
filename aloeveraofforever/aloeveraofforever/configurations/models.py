from django.db import models

# Create your models here.
class Configuration(models.Model):
    name = models.CharField(max_length=32, unique=True)
    value = models.TextField()
    
    class Meta:
        verbose_name_plural = 'Configuration Entries'
        db_table = "configuration"

    def __unicode__(self):
        return '%s - %s' % (self.name, self.value)
