from django.core.management.base import BaseCommand, CommandError
from documents.models import *

from django.conf import settings
from django.utils.encoding import smart_unicode

from documents import layout_scanner
import os
import hashlib
import time, datetime
import subprocess

DOCS_ROOT = settings.MEDIA_ROOT + '/documents/'


class Command(BaseCommand):
    args = 'folder'
    help = 'Searches the folder path for new documents'

    def handle(self, *args, **options):
        for folder in args:
            self.stdout.write('This is folder "%s"\n' % folder)
            os.chdir(folder)
            for files in os.listdir("."):
                if files.endswith(".pdf"):
                    old_document = Document.objects.filter(md5hash=md5(files))
                    if old_document:
                        self.stdout.write("File %s is allready in the databse\n" % files)
                    else:
                        self.stdout.write("Scanning file %s\n" % files)
                        document_pages=layout_scanner.get_pages(files)
                        i = 1
                        pages_for_doc = []
                        for document_page in document_pages:
                            page = Page(number = i, content = smart_unicode(document_page, encoding='utf-8', strings_only=False, errors='strict'))
                            page.save()
                            pages_for_doc.append(page)
                            i = i + 1
                        info = layout_scanner.get_info(files)
                        if 'Title' in info:
                           title = info['Title']
                        else:
                            title = files
                        document = Document(title=title, version=1)
                        document.save()
                        document.pages = pages_for_doc
                        document.md5hash = md5(files)
                        time_format = "D:%Y%m%d%H%M%S"
                        time_string_created = info['CreationDate'].split('Z')
                        time_string_created = time_string_created[0].split('+')
                        time_string_created = time_string_created[0].split('-')
                        document.documentCreated = datetime.datetime.fromtimestamp(time.mktime(time.strptime(time_string_created[0], time_format)))
                        time_string_modified = info['ModDate'].split('Z')
                        time_string_modified = time_string_modified[0].split('+')
                        time_string_modified = time_string_modified[0].split('-')
                        document.documentModified = datetime.datetime.fromtimestamp(time.mktime(time.strptime(time_string_modified[0], time_format)))
                        document.save()
                        author_name = ""
                        if 'Author' in info:
                            author_name = info['Author']
                        else:
                            author_name = "Unbekannter Autor"
                        print author_name
                        author = Author.objects.filter(name=author_name)
                        if author:
                            document.author = author[0]
                            document.save()
                        else:
                            new_author = Author(name=author_name)
                            new_author.save()
                            document.author = new_author
                            document.save()
                        year_string = "%i" % document.documentCreated.year
                        year_category = Category.objects.filter(title=year_string)
                        if year_category:
                            document.categories.add(year_category[0])
                            document.save()
                        else: 
                            new_category = Category(title=year_string)
                            new_category.save()
                            document.categories.add(new_category)
                            document.save()
                        if not os.path.exists(DOCS_ROOT + document.slug ):
                            os.makedirs(DOCS_ROOT + document.slug)
                        file_name = smart_unicode(files, encoding='utf-8', strings_only=False, errors='strict')
                        outcode = subprocess.Popen(u"convert -quality 90% '"  + file_name + "' " + DOCS_ROOT + document.slug + "/" + document.slug + ".jpg", shell=True)
                        while outcode.poll() == None:
                            pass
                        
                        if outcode.poll() == 0:
                            print("Images created for document %s\n" % document.title)
                        else:
                            print("Images could not be created\n")

def md5(fileName, excludeLine="", includeLine=""):
    """Compute md5 hash of the specified file"""
    m = hashlib.md5()
    try:
        fd = open(fileName,"rb")
    except IOError:
        print "Unable to open the file in readmode:", filename
        return
    content = fd.readlines()
    fd.close()
    for eachLine in content:
        if excludeLine and eachLine.startswith(excludeLine):
            continue
        m.update(eachLine)
    m.update(includeLine)
    return m.hexdigest()
