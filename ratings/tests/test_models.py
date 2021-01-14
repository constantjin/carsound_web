from django.test import TestCase

from subjects.models import Subject
from sounds.models import RunSound, EmotionalSound
from ..models import Rating


class TestModels(TestCase):
    def setUp(self):
        self.subject = Subject.objects.create(subject_id=0, name="John Doe")
        self.run_sound = RunSound.objects.create(name="base", url="")
        self.emotional_sound = EmotionalSound.objects.create(
            name="101", url="http://example.com/101.wav"
        )
        self.rating = Rating.objects.create(
            subject=self.subject,
            run=self.run_sound,
            emotional=self.emotional_sound,
            arousal=1,
            dominance=2,
            valence=3,
        )
        self.rating_time = self.rating.created_at.strftime("%Y.%m.%d")

    def test_model_str(self):
        expected_str = (
            f"S0 / Run-base / Emotional-101 / A-1 / D-2 / V-3 / @{self.rating_time}"
        )
        self.assertEqual(str(self.rating), expected_str)

    def test_many_to_one(self):
        another_run = RunSound.objects.create(
            name="gamma_bi", url="http://example.com/gamma_bi.wav"
        )
        another_emotional = EmotionalSound.objects.create(
            name="201", url="https://example.com/201.wav"
        )
        Rating.objects.create(
            subject=self.subject,
            run=another_run,
            emotional=another_emotional,
            arousal=2,
            dominance=4,
            valence=6,
        )
        self.assertEqual(Subject.objects.get(subject_id=0).rating_set.count(), 2)
        self.assertEqual(
            RunSound.objects.get(name="gamma_bi").rating_set.first().arousal, 2
        )
