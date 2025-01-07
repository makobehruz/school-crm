from django.db import models
from groups.models import Group


class Students(models.Model):
    ismi = models.CharField(max_length=100)
    familiya = models.CharField(max_length=100)
    manzil = models.TextField()
    telefon = models.CharField(max_length=13)
    guruh = models.ForeignKey(Group, on_delete=models.CASCADE, related_name='students')
    dob = models.DateField(null=True)
    rasm = models.ImageField(upload_to='student_image/')

    def __str__(self):
        return f"{self.ismi} {self.familiya}"

