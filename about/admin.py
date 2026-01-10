from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import About

# Register your models here.
# admin.site.register(About, SummernoteModelAdmin)


@admin.register(About)
class AboutAdmin(SummernoteModelAdmin):
    """
    Lists fields for display in admin, fields for search, and fields
    with rich-text editor.
    """
    list_display = ('title', 'updated_on')
    search_fields = ['title', 'content']
    summernote_fields = ('content',)
