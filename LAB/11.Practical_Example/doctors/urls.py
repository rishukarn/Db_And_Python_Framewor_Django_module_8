from django.urls import path
from .views import (
    doctor_list, doctor_detail,
    doctor_create, doctor_update,
    doctor_delete, toggle_availability
)

urlpatterns = [
    path('', doctor_list, name='doctor-list'),
    path('<int:pk>/', doctor_detail, name='doctor-detail'),
    path('new/', doctor_create, name='doctor-create'),
    path('<int:pk>/edit/', doctor_update, name='doctor-update'),
    path('<int:pk>/delete/', doctor_delete, name='doctor-delete'),
    path('<int:pk>/toggle/', toggle_availability, name='doctor-toggle'),
]