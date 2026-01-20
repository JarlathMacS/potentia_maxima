from django.test import TestCase
from .forms import FreeConsultationForm


class TestFreeConsultationForm(TestCase):

    def test_form_is_valid(self):
        """ Test for all fields"""
        form = FreeConsultationForm({
            'name': 'Paddy',
            'email': 'test@test.ie',
            'message': 'Howya!'
        })
        self.assertTrue(form.is_valid(), msg="Form is not valid")

    def test_name_is_required(self):
        """Test for the 'name' field"""
        form = FreeConsultationForm({
            'name': '',
            'email': 'test@test.ie',
            'message': 'Howya!'
        })
        self.assertFalse(
            form.is_valid(),
            msg="Name was not provided, but the form is valid"
        )

    def test_email_is_required(self):
        """Test for the 'email' field"""
        form = FreeConsultationForm({
            'name': 'Paddy',
            'email': '',
            'message': 'Howya!'
        })
        self.assertFalse(
            form.is_valid(),
            msg="Email was not provided, but the form is valid"
        )

    def test_message_is_required(self):
        """Test for the 'message' field"""
        form = FreeConsultationForm({
            'name': 'Paddy',
            'email': 'test@test.ie',
            'message': ''
        })
        self.assertFalse(
            form.is_valid(),
            msg="Message was not provided, but the form is valid"
        )
