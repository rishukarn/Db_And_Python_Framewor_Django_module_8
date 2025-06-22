from django.db import models

class Doctor(models.Model):
    SPECIALIZATION_CHOICES = [
        ('GP', 'General Practitioner'),
        ('CAR', 'Cardiologist'),
        ('DER', 'Dermatologist'),
        ('PED', 'Pediatrician'),
    ]
    
    name = models.CharField(max_length=100)
    specialization = models.CharField(max_length=3, choices=SPECIALIZATION_CHOICES)
    contact_number = models.CharField(max_length=15)
    email = models.EmailField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name} ({self.get_specialization_display()})"