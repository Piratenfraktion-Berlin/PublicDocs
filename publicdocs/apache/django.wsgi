import os
import site
import sys

sys.path.append('/opt')
sys.path.append('/opt/publicdocs')
sys.path.append('/opt/publicdocs/PublicDocs')
sys.path.append('/opt/publicdocs/PublicDocs/publicdocs')

site.addsitedir('/opt/publicdocs/lib/python2.6/site-packages')

os.environ['DJANGO_SETTINGS_MODULE'] = 'publicdocs.settings'

import django.core.handlers.wsgi

application = django.core.handlers.wsgi.WSGIHandler()
