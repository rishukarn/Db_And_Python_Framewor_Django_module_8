from django.db import models

# Create your models here.
class Doctor(models.Model):
    SPECIALIZATION_CHOICES = [
        ('GP', 'General Practitioner'),
        ('CAR', 'Cardiologist'),
        ('DER', 'Dermatologist'),
        ('PED', 'Pediatrician'),
        ('ORT', 'Orthopedist'),
        ('NEU', 'Neurologist'),
        ('ONC', 'Oncologist'),
        ('PSY', 'Psychiatrist'),
        ('RAD', 'Radiologist'),
        ('SUR', 'Surgeon'),
    ]
    
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    specialization = models.CharField(max_length=3, choices=SPECIALIZATION_CHOICES)
    contact_number = models.CharField(max_length=15)
    email = models.EmailField(unique=True)
    address = models.TextField()
    license_number = models.CharField(max_length=50, unique=True)
    years_of_experience = models.PositiveIntegerField()
    is_available = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Dr. {self.first_name} {self.last_name} ({self.get_specialization_display()})"

    class Meta:
        ordering = ['last_name', 'first_name']