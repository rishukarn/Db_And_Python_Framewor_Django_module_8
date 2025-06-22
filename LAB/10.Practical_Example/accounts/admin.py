from django.contrib import admin
from .models import UserProfile
# Register your models here.

@admin.register(UserProfile)
class RegisterAdmin(admin.ModelAdmin):
    list_display=['name','email','phone_number','password']