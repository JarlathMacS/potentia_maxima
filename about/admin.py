from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import About

# Register your models here.
# admin.site.register(About, SummernoteModelAdmin)


@admin.register(About)
class AboutAdmin(SummernoteModelAdmin):
    """
    Adds rich-text editing of about content in admin
    """
    list_display = ('title', 'updated_on')
    search_fields = ['title', 'content']
    summernote_fields = ('content',)
