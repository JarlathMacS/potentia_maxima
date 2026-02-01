from django.test import TestCase
from django.urls import reverse


class TestEnquireView(TestCase):

    def test_successful_free_consultation_request_submission(self):
        """Test for submitting a free consultation request"""
        post_data = {
            'name': 'Barney Q Test',
            'email': 'test@test.ie',
            'message': 'Howya!'
        }
        response = self.client.post(reverse(
            'enquire'), post_data)
        self.assertEqual(response.status_code, 200)
        self.assertIn(
            b'Free consultation request received! '
            b'I aim to respond within 3 working days.',
            response.content
        )
