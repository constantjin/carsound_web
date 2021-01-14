from django.test import TestCase

from ..models import Subject


class TestModels(TestCase):
    def test_model_str(self):
        s0 = Subject.objects.create(subject_id=0, name="홍길동")
        s0_time = s0.created_at.strftime("%Y.%m.%d")
        s1 = Subject.objects.create(subject_id=1, name="John Doe")
        s1_time = s1.created_at.strftime("%Y.%m.%d")

        self.assertEqual(str(s0), f"S0 / 홍길동 / {s0_time}")
        self.assertEqual(str(s1), f"S1 / John Doe / {s1_time}")
