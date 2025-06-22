from django.urls import path
from doctors.views import doctor_list

urlpatterns = [
    path('',doctor_list,name='doctor')
]
