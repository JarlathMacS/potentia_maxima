from django.urls import path
from . import views


urlpatterns = [
    path('', views.enquire_view, name='enquire'),
]
