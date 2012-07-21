from django.shortcuts import render_to_response, get_object_or_404, redirect
from django.template import RequestContext

from documents.models  import *

def index(request):
    categories = Category.objects.all()
    return render_to_response('documents/index.html',{'categories': categories},
                            context_instance=RequestContext(request))
