from django.shortcuts import render, redirect, get_object_or_404
from django.core.paginator import Paginator
from .models import Doctor
from .forms import DoctorForm

def doctor_list(request):
    doctors_list = Doctor.objects.all().order_by('last_name', 'first_name')
    
    # Pagination
    paginator = Paginator(doctors_list, 10)  # Show 10 doctors per page
    page_number = request.GET.get('page')
    doctors = paginator.get_page(page_number)
    
    return render(request, 'doctors/doctor_list.html', {'doctors': doctors})

def doctor_detail(request, pk):
    doctor = get_object_or_404(Doctor, pk=pk)
    return render(request, 'doctors/doctor_detail.html', {'doctor': doctor})

def doctor_create(request):
    if request.method == 'POST':
        form = DoctorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('doctor-list')
    else:
        form = DoctorForm()
    
    return render(request, 'doctors/doctor_form.html', {
        'form': form,
        'title': 'Add New Doctor'
    })

def doctor_update(request, pk):
    doctor = get_object_or_404(Doctor, pk=pk)
    
    if request.method == 'POST':
        form = DoctorForm(request.POST, instance=doctor)
        if form.is_valid():
            form.save()
            return redirect('doctor-detail', pk=doctor.pk)
    else:
        form = DoctorForm(instance=doctor)
    
    return render(request, 'doctors/doctor_form.html', {
        'form': form,
        'title': f'Edit Dr. {doctor.first_name} {doctor.last_name}'
    })

def doctor_delete(request, pk):
    doctor = get_object_or_404(Doctor, pk=pk)
    
    if request.method == 'POST':
        doctor.delete()
        return redirect('doctor-list')
    
    return render(request, 'doctors/doctor_confirm_delete.html', {'doctor': doctor})

def toggle_availability(request, pk):
    doctor = get_object_or_404(Doctor, pk=pk)
    doctor.is_available = not doctor.is_available
    doctor.save()
    return redirect('doctor-list')