import random

from django.shortcuts import get_object_or_404

from rest_framework import generics

from subjects.models import Subject
from ratings.models import Rating
from ..models import RunSound, EmotionalSound

from .serializers import RunSoundSerializer, EmotionalSoundSerializer


class GetRunSound(generics.RetrieveAPIView):
    serializer_class = RunSoundSerializer

    def get_object(self):
        subject_pk = self.kwargs.get("subject_pk")

        curr_subject = get_object_or_404(Subject, pk=subject_pk)

        total_runs = [run.id for run in RunSound.objects.all()]
        heard_runs = [
            rating.run.id for rating in Rating.objects.filter(subject=curr_subject)
        ]
        heard_runs = list(set(heard_runs))

        unheard_runs = [id for id in total_runs if id not in heard_runs]
        random_run = random.choice(unheard_runs)

        return get_object_or_404(RunSound, pk=random_run)


class GetEmotionalSound(generics.RetrieveAPIView):
    serializer_class = EmotionalSoundSerializer

    def get_object(self):
        subject_pk = self.kwargs.get("subject_pk")
        run_pk = self.kwargs.get("run_pk")

        curr_subject = get_object_or_404(Subject, pk=subject_pk)
        curr_run = get_object_or_404(RunSound, pk=run_pk)

        total_emotionals = [emotional.id for emotional in EmotionalSound.objects.all()]
        heard_emotionals = [
            rating.emotional.id
            for rating in Rating.objects.filter(subject=curr_subject, run=curr_run)
        ]

        unheard_emotionals = [
            id for id in total_emotionals if id not in heard_emotionals
        ]
        random_emotional = random.choice(unheard_emotionals)

        return get_object_or_404(EmotionalSound, pk=random_emotional)
