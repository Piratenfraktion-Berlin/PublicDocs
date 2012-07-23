from django.db import models

TYPE_CHOICES = (
    (0, 'Version'),
    (1, 'Beziehung'),
    (2, 'Original'),
)

class Document(models.Model):
    title = models.CharField(max_length=254)
    author = models.ForeignKey('documents.Author',null=True,blank=True)
    pages = models.ManyToManyField('documents.Page',null=True)
    version = models.IntegerField(default=1)
    relations = models.ManyToManyField('documents.Relation',null=True,blank=True)
    categories = models.ManyToManyField('documents.Category',null=True,blank=True)
    created = models.DateTimeField(auto_now_add=True,null=True)
    modified = models.DateTimeField(auto_now=True, null=True)

class Page(models.Model):
    number = models.IntegerField()
    content = models.TextField(null=True)
    created = models.DateTimeField(auto_now_add=True,null=True)
    modified = models.DateTimeField(auto_now=True,null=True)

class Paragraph(models.Model):
    content = models.TextField()
    created = models.DateTimeField(auto_now_add=True,null=True)
    modified = models.DateTimeField(auto_now=True,null=True)

class Relation(models.Model):
    type = models.IntegerField(max_length=1, choices=TYPE_CHOICES)
    comment = models.CharField(max_length=500)
    created = models.DateTimeField(auto_now_add=True,null=True)
    modified = models.DateTimeField(auto_now=True,null=True)

class Category(models.Model):
    title = models.CharField(max_length=254)

class Author(models.Model):
    name = models.CharField(max_length=254)
    institution = models.CharField(max_length=254,null=True,blank=True)
    created = models.DateTimeField(auto_now_add=True,null=True)
    modified = models.DateTimeField(auto_now=True,null=True)
