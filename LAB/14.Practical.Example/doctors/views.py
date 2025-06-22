
# Create your views here.
from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from .models import Doctor
from .forms import DoctorForm
from django.template.loader import render_to_string

def doctor_list(request):
    doctors = Doctor.objects.all().order_by('-created_at')
    return render(request, 'doctors/includes/doctor_list.html', {'doctors': doctors})

def save_doctor_form(request, form, template_name):
    data = dict()
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            data['form_is_valid'] = True
            doctors = Doctor.objects.all().order_by('-created_at')
            data['html_doctor_list'] = render_to_string('doctors/includes/partial_doctor_list.html', {
                'doctors': doctors
            })
        else:
            data['form_is_valid'] = False
    context = {'form': form}
    data['html_form'] = render_to_string(template_name, context, request=request)
    return JsonResponse(data)

def doctor_create(request):
    if request.method == 'POST':
        form = DoctorForm(request.POST)
    else:
        form = DoctorForm()
    return save_doctor_form(request, form, 'doctors/includes/partial_doctor_create.html')

def doctor_update(request, pk):
    doctor = get_object_or_404(Doctor, pk=pk)
    if request.method == 'POST':
        form = DoctorForm(request.POST, instance=doctor)
    else:
        form = DoctorForm(instance=doctor)
    return save_doctor_form(request, form, 'doctors/includes/partial_doctor_update.html')

def doctor_delete(request, pk):
    doctor = get_object_or_404(Doctor, pk=pk)
    data = dict()
    if request.method == 'POST':
        doctor.delete()
        data['form_is_valid'] = True
        doctors = Doctor.objects.all().order_by('-created_at')
        data['html_doctor_list'] = render_to_string('doctors/includes/partial_doctor_list.html', {
            'doctors': doctors
        })
    else:
        context = {'doctor': doctor}
        data['html_form'] = render_to_string('doctors/includes/partial_doctor_delete.html', context, request=request)
    return JsonResponse(data)