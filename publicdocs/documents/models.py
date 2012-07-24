#!/usr/bin/env python
# -*- coding: UTF-8 -*-

from django.db import models
from autoslug import AutoSlugField

TYPE_CHOICES = (
    (0, 'Version'),
    (1, 'Beziehung'),
    (2, 'Original'),
)

class Document(models.Model):
    title = models.CharField(max_length=254)
    slug = AutoSlugField(populate_from='title',unique=True,null=True)
    author = models.ForeignKey('documents.Author',null=True,blank=True)
    pages = models.ManyToManyField('documents.Page',null=True,blank=True, related_name='document')
    version = models.IntegerField(default=1)
    relations = models.ManyToManyField('documents.Relation',null=True,blank=True)
    categories = models.ManyToManyField('documents.Category',null=True,blank=True)
    created = models.DateTimeField(auto_now_add=True,null=True)
    modified = models.DateTimeField(auto_now=True, null=True)
    md5hash = models.CharField(max_length=32,null=True,blank=True)
    documentCreated = models.DateTimeField(null=True,blank=True)
    documentModified = models.DateTimeField(null=True,blank=True)

    def __unicode__(self):
        return u'Dokument %s' % self.title

class Page(models.Model):
    number = models.IntegerField()
    content = models.TextField(null=True)
    created = models.DateTimeField(auto_now_add=True,null=True)
    modified = models.DateTimeField(auto_now=True,null=True)
    
    def __unicode__(self):
        return u'Seite: %i' % self.number

class Paragraph(models.Model):
    content = models.TextField()
    created = models.DateTimeField(auto_now_add=True,null=True)
    modified = models.DateTimeField(auto_now=True,null=True)

class Relation(models.Model):
    type = models.IntegerField(max_length=1, choices=TYPE_CHOICES)
    comment = models.CharField(max_length=500)
    created = models.DateTimeField(auto_now_add=True,null=True)
    modified = models.DateTimeField(auto_now=True,null=True)

    def __unicode__(self):
        return u'Beziehung:  %s' % self.comment

class Category(models.Model):
    title = models.CharField(max_length=254)
    slug = AutoSlugField(populate_from='title',unique=True,null=True)

    def __unicode__(self):
        return u'Kategorie:  %s' % self.title


class Author(models.Model):
    name = models.CharField(max_length=254)
    institution = models.CharField(max_length=254,null=True,blank=True)
    created = models.DateTimeField(auto_now_add=True,null=True)
    modified = models.DateTimeField(auto_now=True,null=True)
    slug = AutoSlugField(populate_from='name',unique=True,null=True)
    
    def __unicode__(self):
        return u'Author: %s' % self.name
