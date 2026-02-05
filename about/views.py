from django.shortcuts import render
from .models import About


def about_view(request):
    """
    Renders the most recent information on the about page.

    Displays an individual instance of :model:`about.About`.

    **Context**
    ``about``
        The most recent instance of :model:`about.About`.

    **Template**
    :template:`about/about.html`
    """
    about_content = About.objects.all().order_by('-updated_on').first()
    context = {
        'about': about_content,
    }
    return render(
        request,
        'about/about.html',
        context
        )
