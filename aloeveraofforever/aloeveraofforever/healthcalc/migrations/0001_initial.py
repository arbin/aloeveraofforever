# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'AppsURLs'
        db.create_table('health_calc_url', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('url', self.gf('django.db.models.fields.TextField')(default='', max_length=500, null=True, blank=True)),
        ))
        db.send_create_signal(u'healthcalc', ['AppsURLs'])


    def backwards(self, orm):
        # Deleting model 'AppsURLs'
        db.delete_table('health_calc_url')


    models = {
        u'healthcalc.appsurls': {
            'Meta': {'ordering': "('url',)", 'object_name': 'AppsURLs', 'db_table': "'health_calc_url'"},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'url': ('django.db.models.fields.TextField', [], {'default': "''", 'max_length': '500', 'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['healthcalc']