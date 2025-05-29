from django.test import TestCase
from django.urls import reverse

class YourAppTests(TestCase):
    def test_homepage_accessible(self):
        response = self.client.get(reverse('home'))  # Replace 'home' with your actual homepage URL name
        self.assertEqual(response.status_code, 200)

    def test_protected_route_access(self):
        response = self.client.get(reverse('protected'))  # Replace 'protected' with your actual protected URL name
        self.assertEqual(response.status_code, 401)  # Expecting unauthorized access

    def test_authenticated_access_to_protected_route(self):
        self.client.login(username='testuser', password='testpassword')  # Use valid credentials
        response = self.client.get(reverse('protected'))  # Replace 'protected' with your actual protected URL name
        self.assertEqual(response.status_code, 200)  # Expecting successful access after login

    # Add more tests as needed for your application functionality