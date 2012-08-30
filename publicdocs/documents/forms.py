from django.forms import ModelForm
from django import forms

from documents.models import Comment, Relation

class CommentForm(ModelForm):
    ''' Used for the comments '''
    class Meta:
        model = Comment
        exclude = ["ip","moderated","document"]
        
class RelationForm(ModelForm):
    ''' Used for adding relations '''
    class Meta:
        model = Relation
        fields = ["type", "relatedDocument", "comment"]