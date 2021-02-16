import json
from django.contrib.auth.models import User
from django.urls import reverse
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.test import APITestCase

from .models import Profile, ProfileStatus
from .api.serializers import ProfileSerializer, ProfileStatusSerializer


class RegistrationTestCase(APITestCase):

    def test_registration(self):
        data = dict(username="testcase", email="test@local.app", password1="gr8_news", password2="gr8_news")
        response = self.client.post("/api/rest-auth/registration/", data=data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)


class ProfileViewSetTestCase(APITestCase):
    list_url = reverse("profile-list")

    def setUp(self):
        self.user = User.objects.create_user(username="testuser", password="asfdsgfdsg2r5$")
        self.token = Token.objects.create(user=self.user)
        self.api_authentication()

    def api_authentication(self):
        self.client.credentials(HTTP_AUTHORIZATION="Token " + self.token.key)

    def test_profile_list_authenticated(self):
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_profile_list_un_authenticated(self):
        self.client.force_authenticate(user=None)
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_profile_detail_retrieve(self):
        response = self.client.get(reverse("profile-detail", args=[1]))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data.get("user"), "testuser")

    def test_profile_update_by_owner(self):
        response = self.client.put(reverse("profile-detail", args=[1]), data=dict(
            city="montreal", bio="incenoman"
        ))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(json.loads(response.content),
                         {'avatar': None,
                          'bio': 'incenoman',
                          'city': 'montreal',
                          'id': 1,
                          'statuses': [],
                          'user': 'testuser'})

    def test_profile_update_by_rando(self):
        random_user = User.objects.create_user(username="random", password="asfdsgfdddsg2r5$")
        self.client.force_authenticate(user=random_user)
        response = self.client.put(reverse("profile-detail", args=[1]), data=dict(
            city="montreal", bio="incenoman"
        ))
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_profile_update_by_anon_user(self):
        self.client.force_authenticate(user=None)
        response = self.client.put(reverse("profile-detail", args=[1]), data=dict(
            city="montreal", bio="incenoman"
        ))
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)


class ProfileStatusViewSetTestCase(APITestCase):
    url = reverse("status-list")

    def setUp(self):
        self.user = User.objects.create_user(username="testuser", password="asfdsgfdsg2r5$")
        self.status = ProfileStatus.objects.create(user_profile=self.user.profile, status_content="la-di-da")
        self.token = Token.objects.create(user=self.user)
        self.api_authentication()

    def api_authentication(self):
        self.client.credentials(HTTP_AUTHORIZATION="Token " + self.token.key)

    def test_profile_status_list_authenticated(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_profile_list_status_un_authenticated(self):
        self.client.force_authenticate(user=None)
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_status_create(self):
        data = dict(status_content="a new status")
        response = self.client.post(self.url, data=data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data.get("user_profile"), "testuser")
        self.assertEqual(response.data.get("status_content"), "a new status")

    def test_single_status_retrieve(self):
        serializer_data = ProfileStatusSerializer(instance=self.status).data
        response = self.client.get(reverse("status-detail", args=[1]))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        response_data = json.loads(response.content)
        self.assertEqual(serializer_data, response_data)

    def test_status_update_owner(self):
        data = dict(status_content="a new status")
        response = self.client.put(reverse("status-detail", args=[1]), data=data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["status_content"], "a new status")

    def test_profile_update_by_rando(self):
        data = dict(status_content="a new status")
        random_user = User.objects.create_user(username="random", password="asfdsgfdddsg2r5$")
        self.client.force_authenticate(user=random_user)
        response = self.client.put(reverse("profile-detail", args=[1]), data=data)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_profile_update_by_anon_user(self):
        data = dict(status_content="a new status")
        self.client.force_authenticate(user=None)
        response = self.client.put(reverse("profile-detail", args=[1]), data=data)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)