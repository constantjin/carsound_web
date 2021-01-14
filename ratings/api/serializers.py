from rest_framework import serializers

# from rest_framework.validators import UniqueTogetherValidator

from ..models import Rating


class RatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rating
        fields = (
            "id",
            "subject",
            "run",
            "emotional",
            "arousal",
            "dominance",
            "valence",
            "created_at",
        )
