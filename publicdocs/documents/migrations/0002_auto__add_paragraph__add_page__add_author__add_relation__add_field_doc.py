# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Paragraph'
        db.create_table('documents_paragraph', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('content', self.gf('django.db.models.fields.TextField')()),
            ('created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, null=True, blank=True)),
            ('modified', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, null=True, blank=True)),
        ))
        db.send_create_signal('documents', ['Paragraph'])

        # Adding model 'Page'
        db.create_table('documents_page', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('number', self.gf('django.db.models.fields.IntegerField')()),
            ('created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, null=True, blank=True)),
            ('modified', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, null=True, blank=True)),
        ))
        db.send_create_signal('documents', ['Page'])

        # Adding M2M table for field paragraphs on 'Page'
        db.create_table('documents_page_paragraphs', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('page', models.ForeignKey(orm['documents.page'], null=False)),
            ('paragraph', models.ForeignKey(orm['documents.paragraph'], null=False))
        ))
        db.create_unique('documents_page_paragraphs', ['page_id', 'paragraph_id'])

        # Adding model 'Author'
        db.create_table('documents_author', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=254)),
            ('institution', self.gf('django.db.models.fields.CharField')(max_length=254, null=True, blank=True)),
            ('created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, null=True, blank=True)),
            ('modified', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, null=True, blank=True)),
        ))
        db.send_create_signal('documents', ['Author'])

        # Adding model 'Relation'
        db.create_table('documents_relation', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('type', self.gf('django.db.models.fields.IntegerField')(max_length=1)),
            ('comment', self.gf('django.db.models.fields.CharField')(max_length=500)),
            ('created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, null=True, blank=True)),
            ('modified', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, null=True, blank=True)),
        ))
        db.send_create_signal('documents', ['Relation'])

        # Adding field 'Document.author'
        db.add_column('documents_document', 'author',
                      self.gf('django.db.models.fields.related.ForeignKey')(to=orm['documents.Author'], null=True),
                      keep_default=False)

        # Adding field 'Document.version'
        db.add_column('documents_document', 'version',
                      self.gf('django.db.models.fields.IntegerField')(default=1),
                      keep_default=False)

        # Adding field 'Document.created'
        db.add_column('documents_document', 'created',
                      self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, null=True, blank=True),
                      keep_default=False)

        # Adding field 'Document.modified'
        db.add_column('documents_document', 'modified',
                      self.gf('django.db.models.fields.DateTimeField')(auto_now=True, null=True, blank=True),
                      keep_default=False)

        # Adding M2M table for field pages on 'Document'
        db.create_table('documents_document_pages', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('document', models.ForeignKey(orm['documents.document'], null=False)),
            ('page', models.ForeignKey(orm['documents.page'], null=False))
        ))
        db.create_unique('documents_document_pages', ['document_id', 'page_id'])

        # Adding M2M table for field relations on 'Document'
        db.create_table('documents_document_relations', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('document', models.ForeignKey(orm['documents.document'], null=False)),
            ('relation', models.ForeignKey(orm['documents.relation'], null=False))
        ))
        db.create_unique('documents_document_relations', ['document_id', 'relation_id'])


    def backwards(self, orm):
        # Deleting model 'Paragraph'
        db.delete_table('documents_paragraph')

        # Deleting model 'Page'
        db.delete_table('documents_page')

        # Removing M2M table for field paragraphs on 'Page'
        db.delete_table('documents_page_paragraphs')

        # Deleting model 'Author'
        db.delete_table('documents_author')

        # Deleting model 'Relation'
        db.delete_table('documents_relation')

        # Deleting field 'Document.author'
        db.delete_column('documents_document', 'author_id')

        # Deleting field 'Document.version'
        db.delete_column('documents_document', 'version')

        # Deleting field 'Document.created'
        db.delete_column('documents_document', 'created')

        # Deleting field 'Document.modified'
        db.delete_column('documents_document', 'modified')

        # Removing M2M table for field pages on 'Document'
        db.delete_table('documents_document_pages')

        # Removing M2M table for field relations on 'Document'
        db.delete_table('documents_document_relations')


    models = {
        'documents.author': {
            'Meta': {'object_name': 'Author'},
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'institution': ('django.db.models.fields.CharField', [], {'max_length': '254', 'null': 'True', 'blank': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '254'})
        },
        'documents.document': {
            'Meta': {'object_name': 'Document'},
            'author': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['documents.Author']", 'null': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'null': 'True', 'blank': 'True'}),
            'pages': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['documents.Page']", 'null': 'True', 'symmetrical': 'False'}),
            'relations': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['documents.Relation']", 'null': 'True', 'symmetrical': 'False'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '254'}),
            'version': ('django.db.models.fields.IntegerField', [], {'default': '1'})
        },
        'documents.page': {
            'Meta': {'object_name': 'Page'},
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'null': 'True', 'blank': 'True'}),
            'number': ('django.db.models.fields.IntegerField', [], {}),
            'paragraphs': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['documents.Paragraph']", 'symmetrical': 'False'})
        },
        'documents.paragraph': {
            'Meta': {'object_name': 'Paragraph'},
            'content': ('django.db.models.fields.TextField', [], {}),
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'null': 'True', 'blank': 'True'})
        },
        'documents.relation': {
            'Meta': {'object_name': 'Relation'},
            'comment': ('django.db.models.fields.CharField', [], {'max_length': '500'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'null': 'True', 'blank': 'True'}),
            'type': ('django.db.models.fields.IntegerField', [], {'max_length': '1'})
        }
    }

    complete_apps = ['documents']