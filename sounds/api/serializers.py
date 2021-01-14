from rest_framework import serializers

from ..models import RunSound, EmotionalSound


class RunSoundSerializer(serializers.ModelSerializer):
    class Meta:
        model = RunSound
        fields = ("id", "name", "url")


class EmotionalSoundSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmotionalSound
        fields = ("id", "name", "url")
