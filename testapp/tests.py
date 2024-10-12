from django.test import TestCase
from rest_framework.test import APITestCase
from django.test import TestCase
from testapp.models import  Item
from django.utils import timezone
from django.db.utils import IntegrityError
from django.db import transaction
from django.urls import reverse
import json
from rest_framework.test import APIClient
from django.test import TestCase,RequestFactory
from django.contrib.auth.models import User

class ProjectTestCase(APITestCase):
        
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.item = Item.objects.create(name="Test Item", desc="A test item", qty=10)
    def tearDown(self):
        pass
        

    def test_01_project_get_one(self):
        """
            Verify the backend get call on project
        """
        self.factory = RequestFactory()
        self.client = APIClient()
        test= self.client.force_authenticate(user=self.user)
        response = self.client.get('/v1/items/1/')
        self.assertEqual(response.status_code, 200)        
        data = json.loads(response.content)
        self.assertEqual(data['id'], 1)

        response = self.client.get('/v1/items/99/')
        self.assertEqual(response.status_code, 404)
        
    def test_02_project_view(self):
        """
            Request all project fields are stored in the backend 
        """
        self.factory = RequestFactory()
        self.client = APIClient()
        test= self.client.force_authenticate(user=self.user)
        response = self.client.get('/v1/items/')
        self.assertEqual(response.status_code, 200)
        project = json.loads(response.content)
        self.assertEqual(len(project), 1)        

        #check project keys from data
        self.assertTrue('id' in project[0].keys())
        self.assertTrue('name' in project[0].keys())
        self.assertTrue('desc' in project[0].keys())
        self.assertTrue('qty' in project[0].keys())

        
    def test_03_projects_delete(self):
        """
            Request delete the projects stored in the backend
        """
        self.factory = RequestFactory()
        self.client = APIClient()
        test= self.client.force_authenticate(user=self.user)
        response = self.client.delete('/v1/items/1/')
        self.assertEqual(response.status_code, 204)
        #Verify the able to get deleted projects throws 404
        response = self.client.get('/v1/items/1/')
        self.assertEqual(response.status_code, 404)

# Import necessary modules
from django.test import TestCase
from django.contrib.auth.models import User

# Define your test case class
class UserModelTest(TestCase):

    def setUp(self):
        # Create a sample user for testing
        self.user = User.objects.create_user(
            username='testuser', 
            email='testuser@example.com', 
            password='testpass123'
        )

    def test_user_creation(self):
        # Test user was created correctly
        user = User.objects.get(username='testuser')
        self.assertEqual(user.username, 'testuser')
        self.assertEqual(user.email, 'testuser@example.com')

    def test_user_password(self):
        # Test user password is set correctly (passwords are hashed in Django)
        user = User.objects.get(username='testuser')
        self.assertTrue(user.check_password('testpass123'))

    def test_user_str(self):
        # Test string representation of the user (this usually returns the username)
        user = User.objects.get(username='testuser')
        self.assertEqual(str(user), 'testuser')

    def test_user_authentication(self):
        # Test if the user can authenticate with correct credentials
        user = self.client.login(username='testuser', password='testpass123')
        self.assertTrue(user)

    def test_user_authentication_fail(self):
        # Test if the user authentication fails with incorrect credentials
        user = self.client.login(username='testuser', password='wrongpassword')
        self.assertFalse(user)



