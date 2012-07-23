from django.core.management.base import BaseCommand, CommandError
from documents.models import *

from documents import layout_scanner
import os

class Command(BaseCommand):
    args = 'folder'
    help = 'Searches the folder path for new documents'

    def handle(self, *args, **options):
        for folder in args:
            self.stdout.write('This is folder "%s"\n' % folder)
            os.chdir(folder)
            for files in os.listdir("."):
                if files.endswith(".pdf"):
                    document_pages=layout_scanner.get_pages(files)
                    i = 1
                    pages_for_doc = []
                    for document_page in document_pages:
                        page = Page(number = i, content = document_page)
                        page.save()
                        pages_for_doc.append(page)
                    document = Document(title='test', pages = pages_for_doc, version = 1)
                    document.save()
                    
