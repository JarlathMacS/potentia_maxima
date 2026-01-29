from django.urls import reverse
from django.test import TestCase


class Custom404Tests(TestCase):

    def test_custom_404_view(self):
        """
        Test the handler404 view is used for an invalid url.
        """
        response = self.client.get('/non-existent-url/')
        self.assertEqual(response.status_code, 404)
        self.assertContains(
            response,
            "Something went wrong, as this page is not found!",
            status_code=404,
        )

    def test_404_for_non_existent_post(self):
        """
        Test the handler404 view is used when a coaching post is not found.
        """
        response = self.client.get(
            reverse('coaching_post_detail', args=['non-existent-slug'])
        )
        self.assertEqual(response.status_code, 404)
        self.assertContains(
            response,
            "Something went wrong, as this page is not found!",
            status_code=404,
        )

    def test_404_for_comment_on_non_existent_post(self):
        """
        Test the handler404 view is used when submitting a progress comment
        on a non-existent coaching post.
        """
        post_data = {
            'body': 'This is a test progress comment.'
        }
        response = self.client.post(reverse(
            'coaching_post_detail', args=['non-existent-slug']), post_data)
        self.assertEqual(response.status_code, 404)
        self.assertIn(
            b'Something went wrong, as this page is not found!',
            response.content
        )
        self.client.logout()



    # def test_custom_500_view(self):
    #     """
    #     Ensure the custom 500 view is used for a server error.
    #     """
    #     response = self.client.get('/url-that-does-not-exist/')
    #     self.assertEqual(response.status_code, 404)
    #     self.assertContains(
    #         response,
    #         "Something went wrong, as this page is not found!",
    #         status_code=404,
    #     )
        # Note: Testing the 500 error page directly is complex because it
        # requires simulating a server error. This test checks the 404 page
        # as a proxy to ensure custom error handling is in place. In a full
        # application, you would implement a more robust test for the 500 error.
