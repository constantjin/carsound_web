import uuid
from django.db import models


class Subject(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    subject_id = models.IntegerField(unique=True)
    name = models.CharField(max_length=30)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["subject_id"]

    def __str__(self):
        created_data = self.created_at.strftime("%Y.%m.%d")
        return f"S{self.subject_id} / {self.name} / {created_data}"
