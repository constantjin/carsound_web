from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse

from ..models import Subject


class TestSubjectAPI(APITestCase):
    def setUp(self):
        Subject.objects.create(subject_id=0, name="Mr. Test")
        self.create_url = reverse("api:register")

    def test_participant_create(self):
        s1 = {
            "subject_id": 1,
            "name": "John Doe",
        }
        response = self.client.post(self.create_url, data=s1)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Subject.objects.get(subject_id=1).name, "John Doe")

    def test_reject_same_subject_id(self):
        previous_count = Subject.objects.count()
        s2 = {
            "participant_id": 0,
            "name": "Miss Fail",
        }
        response = self.client.post(self.create_url, data=s2)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(Subject.objects.count(), previous_count)
