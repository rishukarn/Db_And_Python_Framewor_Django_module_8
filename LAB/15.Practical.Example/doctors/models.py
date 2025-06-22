from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

class Specialization(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True)
    
    def __str__(self):
        return self.name

class Doctor(models.Model):
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    ]
    
    AVAILABILITY_CHOICES = [
        ('A', 'Available'),
        ('B', 'On Break'),
        ('L', 'On Leave'),
        ('U', 'Unavailable'),
    ]
    
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    date_of_birth = models.DateField()
    specialization = models.ForeignKey(Specialization, on_delete=models.PROTECT)
    license_number = models.CharField(max_length=20, unique=True)
    years_of_experience = models.PositiveIntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(70)]
    )
    contact_number = models.CharField(max_length=15)
    email = models.EmailField(unique=True)
    address = models.TextField()
    availability = models.CharField(max_length=1, choices=AVAILABILITY_CHOICES, default='A')
    is_active = models.BooleanField(default=True)
    joined_date = models.DateField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)
    profile_picture = models.ImageField(upload_to='doctor_profiles/', blank=True)
    notes = models.TextField(blank=True)

    def __str__(self):
        return f"Dr. {self.first_name} {self.last_name} ({self.specialization})"
    
    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"
    
    @property
    def age(self):
        from datetime import date
        today = date.today()
        return today.year - self.date_of_birth.year - (
            (today.month, today.day) < (self.date_of_birth.month, self.date_of_birth.day)
        )

    class Meta:
        ordering = ['last_name', 'first_name']
        verbose_name = 'Physician'
        verbose_name_plural = 'Physicians'