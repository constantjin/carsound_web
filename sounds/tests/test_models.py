from django.test import TestCase

from ..models import RunSound, EmotionalSound


class TestModels(TestCase):
    def test_runsound_model_str(self):

        run_sound = RunSound(
            name="gamma_bi", url="http://example.com/static/stims/run/gamma_bi.wav"
        )
        self.assertEqual(str(run_sound), "RUN / gamma_bi")

    def test_emotionalsound_model_str(self):

        emotional_sound = EmotionalSound(
            name="102", url="http://example.com/static/stims/emotional/102.wav"
        )
        self.assertEqual(str(emotional_sound), "EMOTIONAL / 102")
