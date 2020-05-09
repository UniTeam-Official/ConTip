from django.test import TestCase
from rest_framework.test import APIClient

from rest_framework import status


class TestAuth(TestCase):

    def setUp(self):
        self.user = APIClient()
        payload = {
            'email': 'test@test.com',
            'username': 'tester',
            'password': 'testpass',
            're_password': 'testpass',
        }
        creation_response = self.user.post('/api/v1/account/users/', payload);
        self.assertEqual(creation_response.status_code, status.HTTP_201_CREATED)

    def test_user_login(self):
        response = self.user.login(username='tester', password='testpass')
        self.assertTrue(response)
        response = self.user.login(username='tester', password='wrong')
        self.assertFalse(response)
        response = self.user.login(username='wrong', password='testpass')
        self.assertFalse(response)
        response = self.user.login(username='wrong', password='wrong')
        self.assertFalse(response)
        response = self.user.login(username='', password='')
        self.assertFalse(response)

    def test_getting_user_info(self):
        response_login = self.user.post('/api/v1/auth/login/', {'username': 'tester', 'password': 'testpass'})
        self.assertEqual(response_login.status_code, status.HTTP_200_OK)

        token = response_login.json()['access']
        self.user.credentials(HTTP_AUTHORIZATION='JWT ' + token)
        resp = self.user.get('/api/v1/account/users/me/', data={'format': 'json'})
        self.assertEqual(resp.json()['username'], 'tester')
        self.assertEqual(resp.json()['email'], 'test@test.com')
