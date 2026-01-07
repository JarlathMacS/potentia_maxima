from .models import ProgressComment
from django import forms


class CommentForm(forms.ModelForm):
    class Meta:
        model = ProgressComment
        fields = ('body',)
