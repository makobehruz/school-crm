from django.db import models


class Subject(models.Model):
    nomi = models.CharField(max_length=50)

    def __str__(self):
        return self.nomi