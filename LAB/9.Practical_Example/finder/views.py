from django.shortcuts import render

def home(request):
    return render(request, 'finder/home.html', {'title': 'Home'})

def profile(request):
    return render(request, 'finder/profile.html', {'title': 'Doctor Profile'})

def contact(request):
    return render(request, 'finder/contact.html', {'title': 'Contact Us'})