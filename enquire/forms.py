from .models import FreeConsultationRequest
from django import forms


class FreeConsultationForm(forms.ModelForm):
    class Meta:
        model = FreeConsultationRequest
        fields = ('name', 'email', 'message')
