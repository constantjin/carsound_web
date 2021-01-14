from rest_framework import generics

from ..models import Subject
from .serializers import SubjectSerializer


class SubjectCreateAPIView(generics.CreateAPIView):
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer
    lookup_field = "id"
