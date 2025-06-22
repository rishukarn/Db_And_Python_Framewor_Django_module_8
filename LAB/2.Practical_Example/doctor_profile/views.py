from django.shortcuts import render

# Create your views here.

def Doctor_profile(req):
    return render(req,'doctorprofile/doctorprofile.html')