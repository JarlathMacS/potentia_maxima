from .models import FreeConsultationRequest
from django import forms


class FreeConsultationForm(forms.ModelForm):
    """
    Form class for site visitors to request a free consultation.
    """
    class Meta:
        model = FreeConsultationRequest
        fields = (
            'name',
            'email',
            'message'
            )
