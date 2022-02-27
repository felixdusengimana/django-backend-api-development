from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelTests(TestCase):

    def test_create_user_with_email_successful(self):
        """Test Creating user with email is successfully."""
        email = "phelixdusengimana@gmail.com"
        password = "test@123"

        user = get_user_model().objects.create_user(
            email,
            password
        )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))
