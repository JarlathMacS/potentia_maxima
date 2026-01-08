from django.shortcuts import render
from .forms import FreeConsultationForm

# Create your views here.
# def index(request):
#     return HttpResponse("Hello, World!")


def enquire_view(request):
    """Renders the enquire page with a free consultation form.
    Renders the most recent information on the about page.

    Displays an individual instance of :model:`about.About`.

    **Context**
    ``about``
        The most recent instance of :model:`about.About`.

    **Template**
    :template:`about/about.html`
    """
    free_consultation_form = FreeConsultationForm()
    # about_content = About.objects.all().order_by('-updated_on').first()
    # In case there's multiple About instances, get the latest one
    # context = {
    #     'about': about_content,
    # }
    # return render(
    #     request,
    #     'about/about.html',
    #     context
    #     )
    return render(
        request,
        "enquire/enquire.html",
        {
            "free_consultation_form": free_consultation_form
        },
    )
