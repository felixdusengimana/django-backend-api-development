from unittest.mock import patch

from django.test import TestCase
from django.contrib.auth import get_user_model
from ..models import Tag, Ingredient, Recipe, recipe_image_file_path


def sample_user(email="test@gmail.com", password="testpass"):
    """Create a sample user for testing."""
    return get_user_model().objects.create_user(email, password)


class ModelTests(TestCase):
    def test_create_user_with_email_successful(self):
        """Test creating a new user with an email is successful"""
        email = 'test@phelix.com'
        password = 'Password123'
        user = get_user_model().objects.create_user(
            email=email,
            password=password
        )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_new_user_email_normalized(self):
        """Test the email for a new user is normalized."""
        email = "test@PHELIX.COM"
        user = get_user_model().objects.create_user(
            email=email,
            password="1234@121"
        )
        self.assertEqual(user.email, email.lower())

    def test_new_user_invalid_email(self):
        """Test creating user with no email raises error"""
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None, "test@122")

    def test_create_new_super_user(self):
        """Test create super user"""
        user = get_user_model().objects.create_superuser(
            'test@phelix.com',
            'test123'
        )

        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)

    def test_tag_str(self):
        """Test tag string representation."""
        tag = Tag.objects.create(
            user=sample_user(),
            name="Vegan"
        )

        self.assertEqual(str(tag), tag.name)

    def test_ingredients(self):
        """Test the ingredient string representation."""
        ingredient = Ingredient.objects.create(
            user=sample_user(),
            name="Cucumber"
        )
        self.assertEqual(str(ingredient), ingredient.name)

    def test_recipe_str(self):
        """Test the recipe string representation."""
        recipe = Recipe(
            user=sample_user(),
            title="Steak and mushroon souce",
            time_minutes=5,
            price=5.00
        )
        self.assertEqual(str(recipe), recipe.title)

    @patch('uuid.uuid4')
    def test_recipe_filename_uui(self, mock_uuid):
        """Test that image is saved in a correct directory."""
        uuid = 'test-uuid'
        mock_uuid.return_value = uuid
        file_path = recipe_image_file_path(None, 'myimage.jpg')
        exp_path = f"uploads/recipe/{uuid}.jpg"
        self.assertEqual(file_path, exp_path)
