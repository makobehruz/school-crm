from django.db import models


class Group(models.Model):
    nomi = models.CharField(max_length=100)
    sinf = models.CharField(max_length=50)
    bolalar = models.CharField(max_length=50)

    def __str__(self):
        return self.nomi