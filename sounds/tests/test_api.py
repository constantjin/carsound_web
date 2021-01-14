from django.urls import reverse

from rest_framework.test import APITestCase
from rest_framework import status

from subjects.models import Subject
from ratings.models import Rating
from ..models import RunSound, EmotionalSound


class TestSoundsAPI(APITestCase):
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

    def test_get_run(self):
        response = self.client.get(
            reverse("api:get-run", kwargs={"subject_pk": self.subject.id})
        )
        self.assertIn(response.data["name"], ["base", "gamma_bi"])

    def test_get_run_return_404(self):
        response = self.client.get(
            reverse(
                "api:get-run",
                kwargs={"subject_pk": "f92b9e88-d690-4874-99cf-5313dbd0cd0b"},
            )
        )
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_get_run_sample(self):
        Rating.objects.create(
            subject=self.subject,
            run=self.run_base,
            emotional=self.emotional_101,
            arousal=1,
            dominance=2,
            valence=3,
        )
        response = self.client.get(
            reverse("api:get-run", kwargs={"subject_pk": self.subject.id})
        )
        self.assertEqual(response.data["name"], "gamma_bi")

    def test_get_emotional(self):
        response = self.client.get(
            reverse(
                "api:get-emotional",
                kwargs={"subject_pk": self.subject.id, "run_pk": self.run_gamma_bi.id},
            )
        )
        self.assertIn(response.data["name"], ["101", "102"])

    def test_get_emotional_return_404(self):
        response = self.client.get(
            reverse(
                "api:get-emotional",
                kwargs={"subject_pk": self.subject.id, "run_pk": 9999},
            )
        )
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_get_emotional_sample(self):
        Rating.objects.create(
            subject=self.subject,
            run=self.run_gamma_bi,
            emotional=self.emotional_101,
            arousal=1,
            dominance=2,
            valence=3,
        )
        response = self.client.get(
            reverse(
                "api:get-emotional",
                kwargs={"subject_pk": self.subject.id, "run_pk": self.run_gamma_bi.id},
            )
        )
        self.assertEqual(response.data["name"], "102")
