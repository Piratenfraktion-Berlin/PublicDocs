from django.shortcuts import render_to_response, get_object_or_404, redirect
from django.template import RequestContext
from django.db.models import Q
import re

from documents.models  import *

def index(request):
    categories = Category.objects.all()
    authors = Author.objects.all()
    return render_to_response('documents/index.html',{'categories': categories, 'authors': authors},
                            context_instance=RequestContext(request))

def category(request, slug):
    documents = Category.objects.get(slug=slug).document_set.all()
    return render_to_response('documents/category.html',{'documents': documents},context_instance=RequestContext(request))

def author(request, slug):
    documents = Author.objects.get(slug=slug).document_set.all()
    return render_to_response('documents/author.html',{'documents': documents},context_instance=RequestContext(request))

def document(request, slug):
    document = get_object_or_404(Document, slug=slug)
    return render_to_response('documents/document.html',{'document': document}, context_instance=RequestContext(request)) 

def search(request):
    ''' The search view for handling the search using Django's "Q"-class (see normlize_query and get_query)'''
    query_string = ''
    found_pages = None
    if ('q' in request.GET) and request.GET['q'].strip():
        query_string = request.GET['q']
        
        entry_query = get_query(query_string, ['document__title', 'content',])
        
        found_pages = Page.objects.select_related().filter(entry_query).order_by('number')

    return render_to_response('documents/search_results.html',
                          { 'query': query_string, 'pages': found_pages, },
                          context_instance=RequestContext(request))

def normalize_query(query_string,
                    findterms=re.compile(r'"([^"]+)"|(\S+)').findall,
                    normspace=re.compile(r'\s{2,}').sub):
    ''' Splits the query string in invidual keywords, getting rid of unecessary spaces
        and grouping quoted words together.
        Example:
        
        >>> normalize_query('  some random  words "with   quotes  " and   spaces')
        ['some', 'random', 'words', 'with quotes', 'and', 'spaces']
    
    '''
    return [normspace(' ', (t[0] or t[1]).strip()) for t in findterms(query_string)] 

def get_query(query_string, search_fields):
    ''' Returns a query, that is a combination of Q objects. That combination
        aims to search keywords within a model by testing the given search fields.
    
    '''
    query = None # Query to search for every search term        
    terms = normalize_query(query_string)
    for term in terms:
        or_query = None # Query to search for a given term in each field
        for field_name in search_fields:
            q = Q(**{"%s__icontains" % field_name: term})
            if or_query is None:
                or_query = q
            else:
                or_query = or_query | q
        if query is None:
            query = or_query
        else:
            query = query & or_query
    return query 
