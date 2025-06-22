
from django.contrib import admin
from .models import Doctor

class DoctorAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'specialization', 'contact_number', 'is_available')
    list_filter = ('specialization', 'is_available')
    search_fields = ('last_name', 'first_name', 'license_number', 'email')
    ordering = ('last_name', 'first_name')

admin.site.register(Doctor, DoctorAdmin)