# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Configuration'
        db.create_table('configuration', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(unique=True, max_length=32)),
            ('value', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal(u'configurations', ['Configuration'])


    def backwards(self, orm):
        # Deleting model 'Configuration'
        db.delete_table('configuration')


    models = {
        u'configurations.configuration': {
            'Meta': {'object_name': 'Configuration', 'db_table': "'configuration'"},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '32'}),
            'value': ('django.db.models.fields.TextField', [], {})
        }
    }

    complete_apps = ['configurations']