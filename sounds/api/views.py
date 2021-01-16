import random

from django.shortcuts import get_object_or_404
from django.conf import settings

from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from subjects.models import Subject
from ratings.models import Rating
from ..models import RunSound, EmotionalSound

from .serializers import RunSoundSerializer, EmotionalSoundSerializer


class GetRunSound(generics.RetrieveAPIView):
    serializer_class = RunSoundSerializer

    def retrieve(self, request, *args, **kwargs):

        # Check registered subjct
        subject_pk = self.kwargs.get("subject_pk")
        curr_subject = get_object_or_404(Subject, pk=subject_pk)

        # Extract unheard run
        total_runs = [run.id for run in RunSound.objects.all()]
        heard_runs = [
            rating.run.id for rating in Rating.objects.filter(subject=curr_subject)
        ]
        heard_runs = set(heard_runs)  # Use a set to check membership
        unheard_runs = [id for id in total_runs if id not in heard_runs]

        # No unheard run -> 204 No Content
        if not unheard_runs:
            return Response(data={}, status=status.HTTP_204_NO_CONTENT)

        # Random sample and serailzation -> 202 OkK
        random_id = random.choice(unheard_runs)
        random_sound = RunSound.objects.get(pk=random_id)
        serializer = self.get_serializer(random_sound)
        return Response(data=serializer.data)


class GetEmotionalSound(generics.RetrieveAPIView):
    serializer_class = EmotionalSoundSerializer

    def retrieve(self, request, *args, **kwargs):

        # Check registered subjct and run
        subject_pk = self.kwargs.get("subject_pk")
        run_pk = self.kwargs.get("run_pk")
        curr_subject = get_object_or_404(Subject, pk=subject_pk)
        curr_run = get_object_or_404(RunSound, pk=run_pk)

        # Extract unheard emotional
        total_emotionals = [emotional.id for emotional in EmotionalSound.objects.all()]
        heard_emotionals = [
            rating.emotional.id
            for rating in Rating.objects.filter(subject=curr_subject, run=curr_run)
        ]
        heard_emotionals = set(heard_emotionals)  # Use a set to check membership
        unheard_emotionals = [
            id for id in total_emotionals if id not in heard_emotionals
        ]

        # No unheard emotional -> 204 No Content
        if not unheard_emotionals:
            return Response(data={}, status=status.HTTP_204_NO_CONTENT)

        # Random sample and serailzation -> 202 OkK
        random_id = random.choice(unheard_emotionals)
        random_sound = EmotionalSound.objects.get(pk=random_id)
        serializer = self.get_serializer(random_sound)
        return Response(data=serializer.data)


@api_view(["GET"])
def get_base_sound(request):
    data = {"name": "base", "url": settings.BASE_SOUND_URL}
    return Response(data=data, status=status.HTTP_200_OK)
