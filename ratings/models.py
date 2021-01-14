from django.db import models

from subjects.models import Subject
from sounds.models import RunSound, EmotionalSound


RATING_CHOICES = [(0, "No response")] + [(i, str(i)) for i in range(1, 10)]


class Rating(models.Model):
    subject = models.ForeignKey(to=Subject, on_delete=models.CASCADE)
    run = models.ForeignKey(to=RunSound, on_delete=models.CASCADE)
    emotional = models.ForeignKey(to=EmotionalSound, on_delete=models.CASCADE)
    arousal = models.IntegerField(choices=RATING_CHOICES)
    dominance = models.IntegerField(choices=RATING_CHOICES)
    valence = models.IntegerField(choices=RATING_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["subject__subject_id", "created_at"]
        unique_together = ("subject", "run", "emotional")

    def __str__(self):
        created_data = self.created_at.strftime("%Y.%m.%d")
        return (
            f"S{self.subject.subject_id} / Run-{self.run.name} / "
            f"Emotional-{self.emotional.name} / A-{self.arousal} / D-{self.dominance} / "
            f"V-{self.valence} / @{created_data}"
        )
