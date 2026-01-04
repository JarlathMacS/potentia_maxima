from django.urls import path
from . import views

# urlpatterns = [
#     path('', views.index, name='index'),
# ]

urlpatterns = [
    path('', views.CoachingPostList.as_view(), name='home'),
    path(
        '<slug:slug>/',
        views.coaching_post_detail,
        name='coaching_post_detail',
    ),
]
