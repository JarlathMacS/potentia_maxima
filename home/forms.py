from .models import ProgressComment
from django import forms


class CommentForm(forms.ModelForm):
    """
    Form class for client users to submit progress comments on a coaching post.
    """
    class Meta:
        model = ProgressComment
        fields = ('body',)
