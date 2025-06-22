from django.urls import path
from doctor.views import index
urlpatterns = [
    path('',index,name='home')
]