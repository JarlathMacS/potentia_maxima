from django.contrib import admin
from .models import FreeConsultationRequest


@admin.register(FreeConsultationRequest)
class FreeConsultationRequestAdmin(admin.ModelAdmin):
    """
    Lists fields for display in admin, fields for search,
    field filters, and fields for ordering.
    """
    list_display = ('name', 'email', 'message', 'read', 'created_on',)
    list_filter = ('read', 'created_on',)
    search_fields = ('name', 'email', 'message',)
