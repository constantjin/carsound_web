from django.urls import reverse

from rest_framework.test import APITestCase
from rest_framework import status

from subjects.models import Subject
from ratings.models import Rating
from ..models import RunSound, EmotionalSound


class TestRatingsCreateAPI(APITestCase):
    def setUp(self):
        self.subject = Subject.objects.create(subject_id=0, name="John Doe")
        self.run_base = RunSound.objects.create(name="base", url="")
        self.run_gamma_bi = RunSound.objects.create(
            name="gamma_bi", url="http://example.com/gamma_bi.wav"
        )
        self.emotional_101 = EmotionalSound.objects.create(
            name="101", url="http://example.com/101.wav"
        )
        self.emotional_102 = EmotionalSound.objects.create(
            name="102", url="http://example.com/102.wav"
        )
        Rating.objects.create(
            subject=self.subject,
            run=self.run_base,
            emotional=self.emotional_101,
            arousal=1,
            dominance=2,
            valence=3,
        )
        self.ratings_url = reverse("api:ratings")

    def test_rating_create(self):
        rating = {
            "subject": self.subject.id,
            "run": self.run_gamma_bi.id,
            "emotional": self.emotional_101.id,
            "arousal": 2,
            "dominance": 4,
            "valence": 6,
        }
        response = self.client.post(self.ratings_url, data=rating)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Rating.objects.count(), 2)
        self.assertEqual(
            Rating.objects.get(
                subject=self.subject,
                run=self.run_gamma_bi,
                emotional=self.emotional_101,
            ).valence,
            6,
        )

    def test_rating_reject_same_pair(self):
        rating = {
            "subject": self.subject.id,
            "run": self.run_base.id,
            "emotional": self.emotional_101.id,
            "arousal": 2,
            "dominance": 4,
            "valence": 6,
        }
        response = self.client.post(self.ratings_url, data=rating)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
