from django.db import models


class RunSound(models.Model):
    name = models.CharField(unique=True, max_length=30)
    url = models.URLField(unique=True, blank=True, null=True)

    def __str__(self):
        return f"RUN / {self.name}"


class EmotionalSound(models.Model):
    name = models.CharField(unique=True, max_length=30)
    url = models.URLField(unique=True)

    def __str__(self):
        return f"EMOTIONAL / {self.name}"
