from rest_framework import generics

from ..models import Rating
from .serializers import RatingSerializer


class RatingCreateAPIView(generics.CreateAPIView):
    queryset = Rating.objects.all()
    serializer_class = RatingSerializer
