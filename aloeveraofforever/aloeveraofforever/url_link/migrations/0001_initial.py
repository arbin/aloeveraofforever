# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'URLLinks'
        db.create_table('url_link', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('url', self.gf('django.db.models.fields.TextField')(default='', max_length=500, null=True, blank=True)),
            ('link', self.gf('django.db.models.fields.TextField')(default='', max_length=500, null=True, blank=True)),
        ))
        db.send_create_signal(u'url_link', ['URLLinks'])


    def backwards(self, orm):
        # Deleting model 'URLLinks'
        db.delete_table('url_link')


    models = {
        u'url_link.urllinks': {
            'Meta': {'ordering': "('url', 'link')", 'object_name': 'URLLinks', 'db_table': "'url_link'"},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'link': ('django.db.models.fields.TextField', [], {'default': "''", 'max_length': '500', 'null': 'True', 'blank': 'True'}),
            'url': ('django.db.models.fields.TextField', [], {'default': "''", 'max_length': '500', 'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['url_link']