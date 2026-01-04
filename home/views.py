from django.shortcuts import get_object_or_404, render
from django.views import generic
from .models import CoachingPost

# from django.http import HttpResponse


# Create your views here.

# def index(request):
#     return HttpResponse("Hello, world!")

class CoachingPostList(generic.ListView):
    # model = CoachingPost
    template_name = "home/index.html"
    # context_object_name = "object_list"
    paginate_by = 6
    queryset = CoachingPost.objects.filter(status=1).order_by("-created_on")
    # filter by audience / client user

    # queryset = CoachingPost.objects.all().order_by("-created_on")
#     queryset = CoachingPost.objects.filter(
#         author__username='admin').order_by("-created_on")
#     queryset = CoachingPost.objects.filter(
#         author__username='admin', status=1).order_by("-created_on")
    # queryset = CoachingPost.objects.filter(
    #     author__username='admin', status=1).order_by("-created_on")[:3]
#     queryset = CoachingPost.objects.filter(
#         author__username='admin', status=1).order_by("-created_on")[:5]
#     queryset = CoachingPost.objects.filter(
# author__username='admin', status=1).order_by("-created_on")[:10]
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
    # queryset = CoachingPost.objects.all().order_by("-created_on")[:3]
#     queryset = CoachingPost.objects.all().order_by("-created_on")[:5]
#     queryset = CoachingPost.objects.all().order_by(
# "-created_on")[:10]
#     queryset = CoachingPost.objects.all().order_by(
# "-created_on")[:6]  # for pagination testing
#     queryset = CoachingPost.objects.all().order_by(
# "-created_on")[:2]  # for pagination testing
#     queryset = CoachingPost.objects.all().order_by(
# "-created_on")[:4]  # for pagination testing
#     queryset = CoachingPost.objects.all().order_by(
# "-created_on")[:8]  # for pagination testing
#     queryset = CoachingPost.objects.all().order_by(
# "-created_on")[:12]  # for pagination testing
#     queryset = CoachingPost.objects.all().order_by(
# "-created_on")[:15]  # for pagination testing
#     queryset = CoachingPost.objects.all().order_by(
# "-created_on")[:20]  # for pagination testing
#     queryset = CoachingPost.objects.all().order_by(
# "-created_on")[:25]  # for pagination testing
#     queryset = CoachingPost.objects.all().order_by(
# "-created_on")[:30]  # for pagination testing
#     queryset = CoachingPost.objects.all().order_by(
# "-created_on")[:50]  # for pagination testing
#     queryset = CoachingPost.objects.all().order_by(
# "-created_on")[:100]  # for pagination testing
#     queryset = CoachingPost.objects.all().order_by(
# "-created_on")[:200]  # for pagination testing
#     queryset = CoachingPost.objects.all().order_by(
# "-created_on")[:500]  # for pagination testing
#     queryset = CoachingPost.objects.all().order_by(
#         "-created_on")[:1000]  # for pagination testing


def coaching_post_detail(request, slug):
    """
    Display an individual :model:`home.CoachingPost`.

    **Context**

    ``post``
        An instance of :model:`home.CoachingPost`.
    ``comments``
        All approved comments related to the post.
    ``comment_count``
        A count of approved comments related to the post.
    ``comment_form``
        An instance of :form:`home.CommentForm`

    **Template:**

    :template:`home/coaching_post_detail.html`
    """
    queryset = CoachingPost.objects.filter(status=1)
    post = get_object_or_404(queryset, slug=slug)
    # comments = post.comments.all().order_by("-created_on")
    # comment_count = post.comments.count()

    # if request.method == "POST":
    #     comment_form = CommentForm(data=request.POST)
    #     if comment_form.is_valid():
    #         comment = comment_form.save(commit=False)
    #         comment.author = request.user
    #         comment.post = post
    #         comment.save()
    #         messages.add_message(
    #             request, messages.SUCCESS,
    #             'Comment submitted and awaiting approval'
    #         )

    # comment_form = CommentForm()

    return render(
        request,
        "home/coaching_post_detail.html",
        {
            "post": post,
            # "comments": comments,
            # "comment_count": comment_count,
            # "comment_form": comment_form,
         },
    )
