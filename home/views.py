from django.shortcuts import get_object_or_404, render, reverse
from django.views import generic
from django.contrib import messages
from django.http import HttpResponseRedirect
from .models import CoachingPost, ProgressComment
from .forms import CommentForm

# from django.http import HttpResponse


# Create your views here.

# def index(request):
#     return HttpResponse("Hello, world!")

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
    # model = CoachingPost
    template_name = "home/index.html"
    # context_object_name = "object_list"
    paginate_by = 6
    queryset = CoachingPost.objects.filter(status=1).order_by("-created_on")
    # filter by audience / client user

    # queryset = CoachingPost.objects.filter(
    #     author__username='admin', status=1).order_by("-created_on")[:6]
    # # for pagination testing
    # queryset = CoachingPost.objects.filter(
    #     author__username='admin', status=1).order_by("-created_on")[:2]
    # # for pagination testing
    # queryset = CoachingPost.objects.filter(
    #     author__username='admin', status=1).order_by("-created_on")[:4]
    # # for pagination testing
    # queryset = CoachingPost.objects.filter(
    #     author__username='admin', status=1).order_by("-created_on")[:8]
    # # for pagination testing
    # queryset = CoachingPost.objects.filter(
    #     author__username='admin', status=1).order_by("-created_on")[:12]
    # # for pagination testing
    # queryset = CoachingPost.objects.filter(
    #     author__username='admin', status=1).order_by("-created_on")[:15]
    #   # for pagination testing
    # queryset = CoachingPost.objects.filter(
    #     author__username='admin', status=1).order_by("-created_on")[:20]
    #   # for pagination testing
    # queryset = CoachingPost.objects.filter(
    #     author__username='admin', status=1).order_by("-created_on")[:25]
    #   # for pagination testing
    # queryset = CoachingPost.objects.filter(
    #     author__username='admin', status=1).order_by("-created_on")[:30]
    #   # for pagination testing
    # queryset = CoachingPost.objects.filter(
    #     author__username='admin', status=1).order_by("-created_on")[:50]
    #   # for pagination testing
    # queryset = CoachingPost.objects.filter(
    #     author__username='admin', status=1).order_by("-created_on")[:100]
    #   # for pagination testing
    # queryset = CoachingPost.objects.filter(
    #     author__username='admin', status=1).order_by("-created_on")[:200]
    #   # for pagination testing
    # queryset = CoachingPost.objects.filter(
    #     author__username='admin', status=1).order_by("-created_on")[:500]
    #   # for pagination testing
    # queryset = CoachingPost.objects.filter(
    #     author__username='admin', status=1).order_by("-created_on")[:1000]
    #   # for pagination testing
    # queryset = CoachingPost.objects.filter(
    #     author__username='admin', status=1).order_by("-created_on")[:3]
    #   # for testing
    # queryset = CoachingPost.objects.filter(
    #     author__username='admin', status=1).order_by("-created_on")[:1]
    #   # for testing
    # queryset = CoachingPost.objects.filter(
    #     author__username='admin', status=1).order_by("-created_on")[:0]
    #   # for testing
    # queryset = CoachingPost.objects.none()  # for testing no posts available


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
    comments = post.comments.all().order_by("-created_on")
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


# The event_id argument is passed into view from the url. In the view
# we get all the Event records from the database as a queryset. Then
# pass this queryset and the event_id to the get_object_or_404()
# helper function and assign that to a variable event.

# Top Tip: In this case, you could shorten the database request code
# by passing the model directly into the helper function.

# event = get_object_or_404(Event, event_id=event_id)

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
            # comment.approved = False
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
    # queryset = CoachingPost.objects.filter(status=1)
    # post = get_object_or_404(queryset, slug=slug)
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
