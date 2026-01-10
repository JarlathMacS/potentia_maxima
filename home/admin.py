from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import CoachingPost, ProgressComment


@admin.register(CoachingPost)
class CoachingPostAdmin(SummernoteModelAdmin):
    """
    Lists fields for display in admin, fields for search,
    field filters, fields to prepopulate, and fields with rich-text editor.
    """
    list_display = ('title', 'slug', 'status', 'created_on')
    search_fields = ['title', 'content']
    list_filter = ('status', 'created_on',)
    prepopulated_fields = {'slug': ('title',)}
    summernote_fields = ('content',)


# Register your models here.
admin.site.register(ProgressComment)
