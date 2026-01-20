from django.contrib.auth.models import User
from django.urls import reverse
from django.test import TestCase
from .forms import CommentForm
from .models import CoachingPost


class TestHomeViews(TestCase):

    def setUp(self):
        """Set up the test."""
        self.user = User.objects.create_superuser(
            username="myUsername",
            password="myPassword",
            email="test@test.ie"
        )
        self.post = CoachingPost(
            title="Coaching post title",
            author=self.user,
            slug="coaching-post-title",
            excerpt="Coaching post excerpt",
            content="Coaching post content",
            status=1
        )
        self.post.save()

    def test_render_coaching_post_detail_page_with_comment_form(self):
        """Test the coaching_post_detail view."""
        self.client.force_login(self.user)
        response = self.client.get(reverse(
            'coaching_post_detail', args=['coaching-post-title']))
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Coaching post title", response.content)
        self.assertIn(b"Coaching post content", response.content)
        self.assertIsInstance(
            response.context['comment_form'], CommentForm)
        self.client.logout()

    def test_successful_progress_comment_submission(self):
        """Test for submitting a progress comment on a coaching post"""
        self.client.login(
            username="myUsername", password="myPassword")
        post_data = {
            'body': 'This is a test progress comment.'
        }
        response = self.client.post(reverse(
            'coaching_post_detail', args=['coaching-post-title']), post_data)
        self.assertEqual(response.status_code, 200)
        self.assertIn(
            b'Your progress comment has been added successfully',
            response.content
        )
        self.client.logout()
