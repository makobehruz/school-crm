from django.db import models


class Teachers(models.Model):
    ismi = models.CharField(max_length=100)
    familiya = models.CharField(max_length=100)
    fan = models.CharField(max_length=50)
    telefon = models.CharField(max_length=13)
    email = models.EmailField(unique=True)
    ish = models.PositiveIntegerField()
    rasm = models.ImageField(upload_to='teachers_image/')

    def __str__(self):
        return f"{self.ismi} {self.familiya}"
