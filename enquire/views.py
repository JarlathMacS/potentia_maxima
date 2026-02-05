from django.contrib import messages
from django.shortcuts import render
from .forms import FreeConsultationForm


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
    if request.method == "POST":
        free_consultation_form = FreeConsultationForm(data=request.POST)
        if free_consultation_form.is_valid():
            free_consultation_form.save()
            messages.add_message(
                request, messages.SUCCESS,
                "Free consultation request received! "
                "I aim to respond within 3 working days.")
        else:
            messages.add_message(
                request, messages.ERROR,
                "There was an error with your request. "
                "Please check the form and try again.")

    free_consultation_form = FreeConsultationForm()

    return render(
        request,
        "enquire/enquire.html",
        {
            "free_consultation_form": free_consultation_form
        },
    )
