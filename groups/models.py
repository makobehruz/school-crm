from django.db import models
from teachers.models import Teachers


class Group(models.Model):
    nomi = models.CharField(max_length=100)
    sinf = models.OneToOneField(Teachers, on_delete=models.CASCADE, related_name='sinf')

    def __str__(self):
        return self.nomi