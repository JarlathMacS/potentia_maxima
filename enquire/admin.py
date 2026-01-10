from django.contrib import admin
from .models import FreeConsultationRequest


# Register your models here.

# Note: admin.ModelAdmin is the standard way of registering
#       our model with the admin panel. We do it differently
#       above because we are supplying Summernote fields.
#       If you want to customise the admin panel view in your
#       own projects, then inherit from admin.ModelAdmin like
#       we do below.


@admin.register(FreeConsultationRequest)
class FreeConsultationRequestAdmin(admin.ModelAdmin):
    """
    Lists fields for display in admin, fields for search,
    field filters, and fields for ordering.
    """
    list_display = ('message', 'read',)
    list_filter = ('read',)
    search_fields = ('message',)
    ordering = ('-read',)
