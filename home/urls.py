from django.urls import path
from . import views


urlpatterns = [
    path('', views.CoachingPostList.as_view(), name='home'),
    path('<slug:slug>/',
         views.coaching_post_detail, name='coaching_post_detail',),
    path('<slug:slug>/edit_comment/<int:comment_id>',
         views.progress_comment_edit, name='progress_comment_edit'),
    path('<slug:slug>/delete_comment/<int:comment_id>',
         views.progress_comment_delete, name='progress_comment_delete'),
]
