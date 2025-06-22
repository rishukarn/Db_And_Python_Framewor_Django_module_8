from django.urls import path
from doctor_profile.views import Doctor_profile
urlpatterns = [
    path('',Doctor_profile,name='profile' ),
]
