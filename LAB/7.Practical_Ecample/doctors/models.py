
from django.db import models

class Doctor(models.Model):
    name = models.CharField(max_length=100)
    specialization = models.CharField(max_length=100)
    experience_years = models.PositiveIntegerField()
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    bio = models.TextField()
    image = models.ImageField(upload_to='doctors/', blank=True, null=True)

    def __str__(self):
        return self.name
