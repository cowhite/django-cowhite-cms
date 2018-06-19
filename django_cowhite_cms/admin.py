from django.contrib import admin
from django.conf import settings

from .models import *


class PageAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'status', 'allow_comments', 'author')
    search_fields = ('title', 'content')

    class Media:
        css = {
            'all': (
                '%sdjango_cowhite_cms/lib/bootstrap-3.3.7-dist/css/bootstrap.min.css' % settings.STATIC_URL,
                '%sdjango_cowhite_cms/lib/summernote/summernote.css' % settings.STATIC_URL,)
        }
        js = [
            '%sdjango_cowhite_cms/lib/js/jquery.min.js' % settings.STATIC_URL,
            '%sdjango_cowhite_cms/lib/bootstrap-3.3.7-dist/js/bootstrap.min.js' % settings.STATIC_URL,
            '%sdjango_cowhite_cms/lib/summernote/summernote.js' % settings.STATIC_URL,
            '%sdjango_cowhite_cms/js/page_admin.js' % settings.STATIC_URL
        ]

admin.site.register(Page, PageAdmin)
