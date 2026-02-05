from django.shortcuts import get_object_or_404, render, reverse
from django.views import generic
from django.contrib import messages
from django.http import HttpResponseRedirect
from .models import CoachingPost, ProgressComment
from .forms import CommentForm


class CoachingPostList(generic.ListView):
    """
    Returns all published coaching posts in :model:`home.CoachingPost`
    and displays them in a page of six coaching posts.
    **Context**

    ``queryset``
        All published instances of :model:`home.CoachingPost`
    ``paginate_by``
        Number of posts per page.

    **Template:**

    :template:`home/index.html`
    """
    template_name = "home/index.html"
    paginate_by = 6
    queryset = CoachingPost.objects.filter(status=1).order_by("-created_on")


def coaching_post_detail(request, slug):
    """
    Display an individual :model:`home.CoachingPost`.

    **Context**

    ``post``
        An instance of :model:`home.CoachingPost`.
    ``comments``
        All progress comments related to the coaching post.
    ``comment_count``
        A count of progress comments related to the coaching post.
    ``comment_form``
        An instance of :form:`home.CommentForm`.

    **Template:**

    :template:`home/coaching_post_detail.html`
    """
    queryset = CoachingPost.objects.filter(status=1)
    post = get_object_or_404(queryset, slug=slug)
    comments = post.comments.all().order_by("created_on")
    comment_count = post.comments.count()

    if request.method == "POST":
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.author = request.user
            comment.post = post
            comment.save()
            messages.add_message(
                request, messages.SUCCESS,
                "Your progress comment has been added successfully"
                )
        else:
            messages.add_message(
                request, messages.ERROR,
                "There was an error adding your progress comment"
                )

    comment_form = CommentForm()

    return render(
        request,
        "home/coaching_post_detail.html",
        {
            "post": post,
            "comments": comments,
            "comment_count": comment_count,
            "comment_form": comment_form,
         },
    )


def progress_comment_edit(request, slug, comment_id):
    """
    Display an individual progress comment for edit.

    **Context**

    ``post``
        An instance of :model:`home.CoachingPost`.
    ``comment``
        A single progress comment related to the post.
    ``comment_form``
        An instance of :form:`home.CommentForm`
    """
    if request.method == "POST":
        queryset = CoachingPost.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        comment = get_object_or_404(ProgressComment, pk=comment_id)
        comment_form = CommentForm(data=request.POST, instance=comment)

        if comment_form.is_valid() and comment.author == request.user:
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.save()
            messages.add_message(
                request, messages.SUCCESS,
                'Progress comment updated!'
            )
        else:
            messages.add_message(
                request, messages.ERROR,
                'Error updating progress comment!'
            )

    return HttpResponseRedirect(reverse('coaching_post_detail', args=[slug]))


def progress_comment_delete(request, slug, comment_id):
    """
    Delete an individual progress comment.

    **Context**

    ``post``
        An instance of :model:`home.CoachingPost`.
    ``comment``
        A single progress comment related to the post.
    """
    comment = get_object_or_404(ProgressComment, pk=comment_id)

    if comment.author == request.user:
        comment.delete()
        messages.add_message(
            request, messages.SUCCESS,
            'Progress comment deleted!'
        )
    else:
        messages.add_message(
            request, messages.ERROR,
            'You can only delete your own progress comments!'
        )

    return HttpResponseRedirect(reverse('coaching_post_detail', args=[slug]))
