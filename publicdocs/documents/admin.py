from documents.models import *

from django.contrib import admin


class DocumentAdmin(admin.ModelAdmin):
    list_display = ('title',)

admin.site.register(Document, DocumentAdmin)
admin.site.register(Author)
admin.site.register(Paragraph)
admin.site.register(Page)
admin.site.register(Relation)
admin.site.register(Category)
admin.site.register(Comment)