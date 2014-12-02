# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'ProductsURLs'
        db.create_table('flp_products_url', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('url', self.gf('django.db.models.fields.TextField')(default='', max_length=500, null=True, blank=True)),
        ))
        db.send_create_signal(u'flp', ['ProductsURLs'])


    def backwards(self, orm):
        # Deleting model 'ProductsURLs'
        db.delete_table('flp_products_url')


    models = {
        u'flp.productsurls': {
            'Meta': {'ordering': "('url',)", 'object_name': 'ProductsURLs', 'db_table': "'flp_products_url'"},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'url': ('django.db.models.fields.TextField', [], {'default': "''", 'max_length': '500', 'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['flp']