# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Document'
        db.create_table('documents_document', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=254)),
        ))
        db.send_create_signal('documents', ['Document'])


    def backwards(self, orm):
        # Deleting model 'Document'
        db.delete_table('documents_document')


    models = {
        'documents.document': {
            'Meta': {'object_name': 'Document'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '254'})
        }
    }

    complete_apps = ['documents']