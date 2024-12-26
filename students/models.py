from django.db import models


class Students(models.Model):
    ismi = models.CharField(max_length=100)
    familiya = models.CharField(max_length=100)
    manzil = models.TextField()
    telefon = models.CharField(max_length=13, default="+998 99 999 99 99")
    guruh = models.CharField(max_length=25)
    dob = models.DateField(null=True, blank=True)
    rasm = models.ImageField(upload_to='student_image/', default='images/default.jpg')

    def __str__(self):
        return self.ismi

